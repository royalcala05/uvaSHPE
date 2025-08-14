from django.shortcuts import render
from .models import Alumni


def home(request):
    """Home page view"""
    return render(request, 'index.html')


def eboard(request):
    """E-Board page view"""
    # Get current exec
    current_exec = Alumni.objects.filter(is_current_exec=True).order_by('shpe_status', 'name')
    
    context = {
        'current_exec': current_exec,
        'total_exec': current_exec.count(),
    }
    
    return render(request, 'eBoard.html', context)


def alumni(request):
    """Alumni directory page view"""
    # Get featured alumni first, then all others (excluding current exec to avoid duplication)
    featured_alumni = Alumni.objects.filter(is_featured=True, is_current_exec=False)
    other_alumni = Alumni.objects.filter(is_featured=False, is_current_exec=False)
    
    context = {
        'featured_alumni': featured_alumni,
        'other_alumni': other_alumni,
        'total_alumni': Alumni.objects.filter(is_current_exec=False).count(),
    }
    
    return render(request, 'alumni.html', context)
