from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import SignupForm, ProfileForm
from .models import UserProfile, UserToken
from .serializers import UserProfileSerializer
from item.models import Category, Item
from django.shortcuts import get_object_or_404

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


def index(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Create a UserProfile for the user
            UserProfile.objects.create(user=user)

            # Automatically log in the user after signup
            authenticated_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, authenticated_user)

            return redirect('/dashboard/dashboard.html')
    else:
        form = SignupForm()

    return render(request, 'main/signup.html', {
        'form': form
    })


# Update the login view to use DRF authentication
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        token, _ = UserToken.objects.get_or_create(user=user)
        return Response({'token': token.token})
    else:
        return Response({'detail': 'Invalid username or password'}, status=400)
