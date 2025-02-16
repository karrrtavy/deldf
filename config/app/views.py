from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from .forms import UserRegistrationForm



def index(request):
    return render(request, "index.html")

def sign_in(request):
    return render(request, "sign_in.html")

def sign_up(request):
    return render(request, "sign_up.html")

def profile(request):
    return render(request, "profile.html")

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
def profile_view(request):
    profile_exists = False
    try:
        profile = request.user.userprofile
        profile_exists = True
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile_instance = form.save(commit=False)
            if not profile_exists:
                profile_instance.user = request.user
            profile_instance.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'profile_exists': profile_exists
    }
    return render(request, 'profile.html' if profile_exists else 'profile.html', context)















# Create your views here.