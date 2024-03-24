from django.urls import path
from .views import ChatView, NewMessage
urlpatterns = [
    path('new-chat', ChatView.as_view(), name= 'add-new-chat'),
    path('get-chat/<int:pk>/', ChatView.as_view(), name= 'get-chat'),
    path('get-chat/', ChatView.as_view(), name= 'get-all-chat'),
    path('new-message', NewMessage.as_view(), name= 'add-new-msg'),
    path('get-messages/<int:chat_id>', NewMessage.as_view(), name='get-messages'),
    path('api/chats/<int:id>/', ChatView.as_view()),
]