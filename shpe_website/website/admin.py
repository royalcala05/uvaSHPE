from django.contrib import admin
from .models import Alumni


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    """Admin interface for Alumni model"""
    
    list_display = ['name', 'graduation_year', 'major', 'position', 'company', 'shpe_status', 'is_featured', 'is_current_exec', 'created_at']
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
    
    readonly_fields = []
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ['created_at', 'updated_at']
        return []
