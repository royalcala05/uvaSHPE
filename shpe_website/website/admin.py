from django.contrib import admin
from django.utils.html import format_html
from .models import Alumni
import os


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    """Admin interface for Alumni model"""
    
    list_display = ['name', 'graduation_year', 'major', 'position', 'company', 'shpe_status', 'is_featured', 'is_current_exec', 'created_at', 'headshot_size']
    list_filter = ['graduation_year', 'major', 'shpe_status', 'is_featured', 'is_current_exec', 'created_at']
    search_fields = ['name', 'email', 'major', 'position', 'company']
    list_editable = ['is_featured', 'is_current_exec']
    
    fieldsets = [
        ('Personal Information', {
            'fields': ['name', 'headshot', 'email', 'graduation_year', 'major']
        }),
        ('SHPE Information', {
            'fields': ['shpe_status'],
            'description': 'Role they held while at SHPE UVA'
        }),
        ('Professional Information', {
            'fields': ['position', 'company', 'bio', 'linkedin_url']
        }),
        ('Display Options', {
            'fields': ['is_featured', 'is_current_exec'],
            'description': 'Control how this alumni appears on the website'
        }),
    ]
    
    readonly_fields = ['headshot_size']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ['created_at', 'updated_at', 'headshot_size']
        return ['headshot_size']
    
    def headshot_size(self, obj):
        """Display the file size of the headshot image"""
        if obj.headshot and obj.headshot.storage.exists(obj.headshot.name):
            size_bytes = obj.headshot.size
            if size_bytes < 1024:
                return f"{size_bytes} B"
            elif size_bytes < 1024 * 1024:
                return f"{size_bytes / 1024:.1f} KB"
            else:
                return f"{size_bytes / (1024 * 1024):.1f} MB"
        return "No image"
    
    headshot_size.short_description = "Image Size"
