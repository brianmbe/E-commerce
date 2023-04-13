# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Account
from django.http import HttpResponse

# send email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, EmailMessage

# Registration


def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            user = Account.objects.createUser(
                first_name=first_name, last_name=last_name, email=email, username=first_name, password=password)
            user.phone_number = phone_number
            user.is_active = False  # Mark the user as inactive until email is verified
            user.save()

            # User activation
            current_domain = get_current_site(request).domain
            mail_subject = 'Please activate your account'
            message = render_to_string('account/account_verification.html', {
                'user': user,
                'domain': current_domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(
                request, f'Your account ({email}) has been registered successfully. Please check your email for account verification.')
            return redirect('register')
        else:
            form = RegistrationForm()
            messages.error(
                request, 'Please try again!')

    context = {
        "form": form
    }
    return render(request, "account/register.html", context)


# Account activation
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # Log in the user after successful account activation
        auth.login(request, user)
        messages.success(
            request, 'Congratulations! Your account has been activated and you have been logged in.')
        # Redirect to home page after successful account activation
        return redirect('home')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


# Login
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have been logged in successfully!')
            return redirect('home')
        else:
            messages.error(
                request, 'Please enter the right login credentials')

    return render(request, "account/login.html")


# Logout
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')
