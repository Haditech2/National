from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Album, Video

# Create your views here.

class GalleryView(ListView):
    model = Album
    template_name = 'gallery/gallery.html'
    context_object_name = 'albums'


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'gallery/album_detail.html'
    context_object_name = 'album'


class VideoListView(ListView):
    model = Video
    template_name = 'gallery/video_list.html'
    context_object_name = 'videos'
