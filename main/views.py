from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from item.models import Category, Item
from .forms import SignupForm
from .models import UserProfile

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

            return redirect('/dashboard/dashboard.html')  # Replace with your desired redirect URL
    else:
        form = SignupForm()

    return render(request, 'main/signup.html', {
        'form': form
    })
