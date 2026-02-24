from django.contrib import admin
from django.utils.html import format_html
from .models import Blog, CustomerMessage, TeamMember
from unfold.admin import ModelAdmin

@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'image_tag')
    search_fields = ('title',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"

@admin.register(CustomerMessage)
class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject')

        # Disable the ability to add new entries from admin
    def has_add_permission(self, request):
        return False

    # Keep delete permission
    def has_delete_permission(self, request, obj=None):
        return True

    # Disable change permission (editing) at the model level
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at')
    search_fields = ('name', 'position')