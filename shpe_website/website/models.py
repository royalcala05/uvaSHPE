from django.db import models
from django.core.validators import EmailValidator


class Alumni(models.Model):
    """Model for SHPE UVA Alumni directory"""
    
    name = models.CharField(
        max_length=100,
        help_text="Full name of the alumni"
    )
    
    headshot = models.ImageField(
        upload_to='alumni_photos/',
        blank=True,
        null=True,
        help_text="Professional headshot photo (optional)"
    )
    
    bio = models.TextField(
        help_text="Brief biography and background"
    )
    
    position = models.CharField(
        max_length=200,
        help_text="Current job title or position"
    )
    
    company = models.CharField(
        max_length=200,
        help_text="Current company, university, or organization"
    )
    
    SHPE_STATUS_CHOICES = [
        ('member', 'Member'),
        ('officer', 'Officer'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
        ('vice_president', 'Vice President'),
        ('co_president', 'Co-President'),
        ('president', 'President'),
        ('social_chair', 'Social Chair'),
        ('marketing', 'Marketing'),
        ('corporate_relations', 'Corporate Relations'),
        ('community_outreach', 'Community Outreach'),
        ('convention_chair', 'Convention Chair'),
        ('first_year_rep', 'First Year Representative'),
        ('spiderman', 'WebMaster')
    ]
    
    shpe_status = models.CharField(
        max_length=50,
        choices=SHPE_STATUS_CHOICES,
        default='member',
        help_text="Role they held in SHPE UVA"
    )
    
    email = models.EmailField(
        validators=[EmailValidator()],
        help_text="Contact email address"
    )
    
    major = models.CharField(
        max_length=100,
        help_text="Major studied at UVA"
    )
    
    graduation_year = models.PositiveIntegerField(
        help_text="Year graduated from UVA"
    )
    
    linkedin_url = models.URLField(
        blank=True,
        null=True,
        help_text="LinkedIn profile URL (optional)"
    )
    
    is_featured = models.BooleanField(
        default=False,
        help_text="Show this alumni prominently on the page"
    )
    
    is_current_exec = models.BooleanField(
        default=False,
        help_text="Currently serving on the executive board"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Alumni"
        verbose_name_plural = "Alumni"
        ordering = ['-graduation_year', 'name']
    
    def __str__(self):
        return f"{self.name} (Class of {self.graduation_year})"
