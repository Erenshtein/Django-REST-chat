from rest_framework import serializers
from .models import ChatMessage
import re


class ChatMessageDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for message instances.
    Converts ChatMessage Model to JSON responses.
    """
    class Meta:
        model = ChatMessage
        fields = "__all__"
        read_only_fields = ['id', 'created_ts', 'updated_ts']

    def validate_email(self, value):
        """Email field standart validation."""
        re_result = re.match(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)'
                             r'\.([a-zA-Z]{2,5})$', value)
        if(re_result):
            return value
        else:
            raise serializers.ValidationError('Email address is not valid.')

    def validate_text(self, value):
        """
        Message text field validation.
        That text is not blank and not to long
        """
        re_result = re.match(r'^[\S\s]{1,99}$', value)
        if(re_result):
            return value
        else:
            raise serializers.ValidationError('Message text cannot be blank '
                                              'or longer than 99 characters.')
