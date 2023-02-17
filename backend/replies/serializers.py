from rest_framework import serializers
from .models import Reply

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'username', 'comment_id', 'text']
    username = serializers.SerializerMethodField()
    def get_username(self, reply):
        return reply.user.username
