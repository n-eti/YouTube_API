from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Reply

# from .models import Comment

from .serializers import ReplySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def replies_list(request, comment_id):
    if request.method == 'GET':
        replies = Reply.objects.filter(comment_id=comment_id)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(comment_id=comment_id, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        