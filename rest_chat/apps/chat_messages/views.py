from django.http import Http404
from rest_framework import generics
from .serializers import ChatMessageDetailSerializer
from .models import ChatMessage


class ChatMessageCreateView(generics.CreateAPIView):
    """View for Create new message requests"""
    serializer_class = ChatMessageDetailSerializer


class ChatMessageListView(generics.ListAPIView):
    """View for Listing all messages by pages"""
    serializer_class = ChatMessageDetailSerializer
    lookup_url_kwarg = 'page'
    page_size = 10

    def get_queryset(self):
        page = self.kwargs.get(self.lookup_url_kwarg) * self.page_size
        if(page > ChatMessage.objects.count()):
            raise Http404
        else:
            return ChatMessage.objects.order_by('id')[page:page+10]


class ChatMessageSingleView(generics.RetrieveAPIView):
    """View for Retrieving message instance by id"""
    serializer_class = ChatMessageDetailSerializer
    lookup_field = 'id'

    def get_object(self):
        id = self.kwargs.get(self.lookup_field)
        try:
            return ChatMessage.objects.get(id=id)
        except ChatMessage.DoesNotExist:
            raise Http404
