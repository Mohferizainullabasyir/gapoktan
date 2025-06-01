from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import NIKLoginForm

def login_view(request):
    form = NIKLoginForm(request.POST or None)
    if form.is_valid():
        login(request, form.user)
        # Redirect berdasarkan role
        role = form.user.role
        if role == 'admin':
            return redirect('/admin-dashboard/')
        elif role == 'ketua':
            return redirect('/ketua-dashboard/')
        else:
            return redirect('/petani-dashboard/')
    return render(request, 'login_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
