from django.urls import path
from . import consumers
from . import views

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new_conversation'),
    path('inbox/', views.inbox, name='inbox'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    # Other URL patterns for conversation views
    
]

 # WebSocket URL pattern
websocket_urlpatterns = [
    path('ws/conversation/<int:conversation_id>/', consumers.ChatConsumer.as_asgi()),
]
