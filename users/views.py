from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout


# Home 

def home_view(request):
    return render(request, 'users/home.html')
# Dashboard 

from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html')


from django.contrib.auth import login, get_backends

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Fix for multiple authentication backends
            backend = get_backends()[0]
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            login(request, user)

            return redirect('login')
    else:
        form = CustomUserForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')