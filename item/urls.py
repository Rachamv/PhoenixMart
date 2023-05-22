from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
