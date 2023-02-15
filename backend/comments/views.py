from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.

@api_view(['GET'])
def comments_list(request, video_id):
    comments = Comment.objects.filter(video_id = video_id)

    serializer = CommentSerializer(comments, many = True)


    return Response(serializer.data)
