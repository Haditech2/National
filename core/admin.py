from django.contrib import admin
from .models import Executive

# Register your models here.

@admin.register(Executive)
class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'school', 'phone_number', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'position', 'school')
