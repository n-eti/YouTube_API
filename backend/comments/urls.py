from django.urls import path
from . import views

urlpatterns = [
    path('<str:video_id>/', views.comments_list),
]
