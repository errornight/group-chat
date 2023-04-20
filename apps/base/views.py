from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, EditProfile
from .models import User
from django.contrib.auth.forms import PasswordChangeForm

def startup(request):
    if request.user.is_authenticated:
        return redirect('Profile', request.user.uuid)
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.instance)
            return redirect('Profile', request.user.uuid)

    context = {'form': form}
    return render(request, 'base/signup.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('Profile', request.user.uuid)

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('Profile', request.user.uuid)
    
    context = {'form': form}
    return render(request, 'base/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('Startup')

@login_required
def profile(request, uuid):
    user = get_object_or_404(User, uuid=uuid)
    context = {'user': user}
    return render(request, 'base/profile.html', context)


@login_required()
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('Profile', request.user.uuid)

    return render(request, 'base/edit-profile.html')

@login_required()
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Security:)
            print('Password changed!')
            return redirect('Profile', request.user.uuid)

    context = {'form': form}
    return render(request, 'base/change-password.html', context)
