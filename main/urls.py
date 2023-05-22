from django.contrib.auth import views as auth_views
from django.urls import include, path
from conversation.urls import websocket_urlpatterns

from . import views
from .forms import LoginForm

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html', authentication_form=LoginForm), name='login'),
    
    path('conversation/', include('conversation.urls')),

]
websocket_urlpatterns = [
    # WebSocket URL patterns from the conversation app
    *websocket_urlpatterns,
]
