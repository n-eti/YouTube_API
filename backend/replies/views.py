from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import ReplySerializer
from .models import Reply
# Create your views here.

@api_view(['GET'])
def replies_list(request, comment_id):
    replies = Reply.objects.filter(comment_id=comment_id)
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)
