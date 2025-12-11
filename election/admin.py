from django.contrib import admin
from .models import Candidate

# Register your models here.

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'level', 'department')
    list_filter = ('position', 'level')
    search_fields = ('name', 'department')
