from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def comments_list(request, video_id):
    comments = Comment.objects.filter(video_id = video_id)
    serializer = CommentSerializer(comments, many = True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request):
    print(request)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    serializer = CommentSerializer(comment, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

