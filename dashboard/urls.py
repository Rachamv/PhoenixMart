from django.urls import path, include
from . import views
from conversation.urls import websocket_urlpatterns

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.update_profile, name='update_profile'),
    path('conversation/', include('conversation.urls')),
]

websocket_urlpatterns += [
    # WebSocket URL patterns from the conversation app
    *websocket_urlpatterns,
]
