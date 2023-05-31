from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import SignupForm, ProfileForm
from .models import UserProfile, UserToken
from .serializers import UserProfileSerializer
from item.models import Category, Item
from django.shortcuts import get_object_or_404
from django.contrib import messages

@api_view(['GET'])
def user_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['POST'])
def update_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)

        if form.is_valid():
            form.save()
            return redirect('dashboard:index')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'dashboard/profile.html', {
        'form': form,
    })

@login_required
def home(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'dashboard/home.html', {
        'categories': categories,
        'items': items,
    })

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'main/index.html', {
        'categories': categories,
        'items': items,
    })
    
def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')

# Update the login view to use DRF authentication
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        token, _ = UserToken.objects.get_or_create(user=user)
        messages.success(request, 'You have successfully logged in.')
        return redirect('dashboard:home')
    else:
        messages.error(request, 'Invalid username or password. Please try again.')
        return redirect('main:login')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            # Check if username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect('main:signup')

            # Create new user
            user = form.save(commit=False)
            user.set_password(password)
            user.save()

            authenticated_user = authenticate(username=username, password=password)

            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, 'You have successfully registered and logged in.')
                return redirect('dashboard:index')
            else:
                messages.error(request, 'An error occurred during registration. Please try again.')
                return redirect('main:signup')
    else:
        form = SignupForm()

    return render(request, 'main/signup.html', {'form': form})
    return render(request, 'main/signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('main:index')