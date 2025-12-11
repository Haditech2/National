from django.contrib import admin
from .models import Member

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_id', 'school', 'level', 'chapter')
    list_filter = ('school', 'level', 'chapter')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'membership_id')
    readonly_fields = ('membership_id', 'qr_code_image', 'id_card_generated_at')
