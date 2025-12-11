from django.contrib import admin
from .models import Album, Photo, Video

# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    search_fields = ('title',)
    inlines = [PhotoInline]

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)
