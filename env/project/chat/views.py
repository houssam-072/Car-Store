from rest_framework.response import Response
from rest_framework import status
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from accounts.models import User
from rest_framework.generics import GenericAPIView


class ChatView(GenericAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        return Chat.objects.all()
    
    def post(self, request, *args, **kwargs):
        receiver_id = request.data.get('receiver_id')
        recipient_id = request.data.get('recipient_id')

        try:
            receiver = User.objects.get(email=receiver_id)
            recipient = User.objects.get(id=recipient_id)

        except User.DoesNotExist:
            return Response({"error": "One or both users not found"}, status=status.HTTP_404_NOT_FOUND)
        
        chat = Chat.objects.create(receiver=receiver, recipient=recipient)
        serializer = self.serializer_class(chat)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk = None):
        if pk is not None:
            try:
                chat = Chat.objects.get(pk = pk)
            except Chat.DoesNotExist:
                return Response({'error': 'chat not found'}, status=status.HTTP_404_NOT_FOUND)   
            serializer = self.serializer_class(chat)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            chat_list =self.get_queryset()
            serializer = self.serializer_class(chat_list, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        

    def patch(self, request, *args, **kwargs):
        chat_id = kwargs.get('chat_id')
        try:
            chat = Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ChatSerializer(chat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(read=True)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewMessage(GenericAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()  # Set the queryset attribute to all messages

    def post(self, request, *args, **kwargs):
        chat_id = request.data.get('chat_id')
        sender_id = request.data.get('sender_id')
        content = request.data.get('content')

        try:
            chat = Chat.objects.get(id=chat_id)
            sender = User.objects.get(id=sender_id)
        except (Chat.DoesNotExist, User.DoesNotExist):
            return Response({"error": "Chat or sender not found"}, status=status.HTTP_404_NOT_FOUND)

        message = Message.objects.create(chat=chat, sender=sender, content=content)
        serializer = self.serializer_class(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, chat_id, *args, **kwargs):
        try:
            chat = Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            return Response({"error": "Chat not found"}, status=status.HTTP_404_NOT_FOUND)

        messages = chat.messages.all()  # Retrieve all messages for the given chat
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)