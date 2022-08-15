from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_messages , name='messages'),
    path('get/<slug:key>/', views.get_message, name='message'),
    path('create/', views.Create_Message.as_view(), name='create_message'),
    path('update/<slug:key>/', views.Update_Message.as_view(), name='update_message'),
]
