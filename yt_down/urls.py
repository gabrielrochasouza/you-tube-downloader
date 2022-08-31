from django.urls import path
from yt_down import views

urlpatterns = [
    path("", views.main_page),
    path("video/", views.download_video_page),
    path("video/download/", views.download_video),
    path("video/download/downloaded/", views.video_downloaded),
    path("mp3/", views.download_mp3_page),
]
