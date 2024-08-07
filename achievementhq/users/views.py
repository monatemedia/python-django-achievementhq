from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm  # Import your custom form
from django.contrib.auth import logout as auth_logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # Use the custom form
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Pass `request` to form
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Welcome {user.username}!!')
            return redirect('polls:user_list')
        else:
            messages.info(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form, 'title': 'Login'})


def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('pages:index')  # Redirect to the logged out index page