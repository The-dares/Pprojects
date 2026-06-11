from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
def home(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        Profile.objects.create(user=user, phone=phone)

        return redirect('login')

    return render(request, 'register.html')
@login_required
def dashboard(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, 'dashboard.html', {
        'user': request.user,
        'profile': profile
    })
@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, 'profile.html', {
        'user': request.user,
        'profile': profile
    })