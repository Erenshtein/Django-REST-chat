from django.urls import path
from . import views


app_name = 'chat_messages'
urlpatterns = [
    path('create/', views.ChatMessageCreateView.as_view(), name='create'),
    path('list/<int:page>/', views.ChatMessageListView.as_view(), name='list'),
    path('single/<int:id>/', views.ChatMessageSingleView.as_view(),
         name='single'),
]
