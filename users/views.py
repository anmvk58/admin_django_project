from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {
        'form': form
    })

@login_required(login_url='/user/login')
def home(request):
    return render(request, 'users/home.html')
