from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.forms import SignupForm, ProfileForm
from main.models import UserProfile, UserToken
from main.serializers import UserProfileSerializer
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

@login_required
def logout_view(request):
    logout(request)
    return redirect('main:index')


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)  
    return render(request, 'item/item_detail.html', {'item': item})

from django.shortcuts import render, redirect
from .forms import ItemForm

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect('item:item_detail', pk=item.pk)  
    else:
        form = ItemForm()
    return render(request, 'item/create_item.html', {'form': form})

def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('item:item_detail.html', pk=item.pk) 
    else:
        form = ItemForm(instance=item)
    return render(request, 'item/update_item.html', {'form': form})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item:item_list.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)  
    return render(request, 'category/category_detail.html', {'category': category})



