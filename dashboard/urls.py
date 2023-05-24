from . import views
from django.urls import path, include
from conversation.urls import websocket_urlpatterns

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('order/create/', views.create_order, name='create_order'),
    path('order/update/<int:pk>/', views.update_order, name='update_order'),
    path('payment/create/', views.create_payment, name='create_payment'),
    path('payment/update/<int:pk>/', views.update_payment, name='update_payment'),
    path('delivery/create/', views.create_delivery, name='create_delivery'),
    path('delivery/update/<int:pk>/', views.update_delivery, name='update_delivery'),
    path('support-ticket/create/', views.create_support_ticket, name='create_support_ticket'),
    path('support-ticket/update/<int:pk>/', views.update_support_ticket, name='update_support_ticket'),
]

urlpatterns += [
    path('ws/', include(websocket_urlpatterns)),
]
