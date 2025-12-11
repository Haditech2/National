from django.contrib import admin
from .models import Event, EventImage

# Register your models here.

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 3

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue', 'is_upcoming')
    list_filter = ('date',)
    search_fields = ('title', 'venue')
    inlines = [EventImageInline]
