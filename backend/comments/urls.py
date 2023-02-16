from django.urls import path, include
from . import views

urlpatterns = [
    path('video/<str:video_id>/', views.comments_list),
    path('', views.add_comment),
    path('<int:comment_id>/', views.edit_comment),
    path('<int:comment_id>/replies/',include('replies.urls')),
]
