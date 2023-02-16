from django.urls import path
from . import views

urlpatterns = [
    path('video/<str:video_id>/', views.comments_list),
    path('', views.add_comment),
    path('<int:comment_id>/', views.edit_comment),
]
