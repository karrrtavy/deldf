from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserProfileForm, UserRegistrationForm
from .models import UserProfile



def index(request):
    return render(request, "index.html")

def sign_in(request):
    return render(request, "sign_in.html")

def sign_up(request):
    return render(request, "sign_up.html")

def polit_konf(request):
    return render(request, "polit_konf.html")



def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sign_in')
    else:
        form = UserRegistrationForm()
    return render(request, 'sign_up.html', {'form': form})



# тут будет функция рассылки сообщений на почту и валидацию def verify_email(request): тд и тп



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('index')



@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile_instance = form.save(commit=False)
            profile_instance.user = user
            profile_instance.save()
            return redirect('profile', username=username)
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'user': user,
    }
    return render(request, 'profile.html', context)
# Create your views here.