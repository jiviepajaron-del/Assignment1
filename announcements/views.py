from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Announcement

def home(request):
    return render(request, 'announcements/home.html')

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    return render(request, 'announcements/announcement_detail.html', {'announcement': announcement})

# Create your views here.
