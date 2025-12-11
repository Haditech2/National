from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.GalleryView.as_view(), name='gallery'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('videos/', views.VideoListView.as_view(), name='video_list'),
]
