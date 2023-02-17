from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Comment
from .serializers import ReplySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Reply
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def replies_list(request, comment_id):
    replies = Reply.objects.filter(comment_id=comment_id)
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)

@api_view (['POST'])
@permission_classes([IsAuthenticated])
def add_reply(request, comment_id):
    print(request)
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
