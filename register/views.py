from django.shortcuts import render, redirect
from .forms import registerForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def register(response):
    if response.user.is_authenticated:
        return redirect('../timeline')
    elif response.method == 'POST':
        form = registerForm(response.POST)
        if form.is_valid():
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            if pass1 != pass2:
                messages.warning(response, 'password doesnot match')
                return redirect('../register')
            elif User.objects.filter(email=email).exists():
                messages.warning(response, 'Email-Id already exists')
                return redirect('../register')
            elif User.objects.filter(username=username).exists():
                messages.warning(response, 'Username already exists')
                return redirect('../register')
            else:
                user = User.objects.create_user(
                    username=username, password=pass1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                messages.info(response, 'Succesfully registered')
                return redirect('../login')
        else:
            messages.error(response, 'invalid form')
            return redirect('../register')
    else:
        form = registerForm()
    return render(response, 'register/register.html', {'form': form})
