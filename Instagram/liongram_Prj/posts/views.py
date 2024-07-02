from django.shortcuts import render
from .models import Post

# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/list.html', {'posts': posts})

def result(request):
    entered_text = request.GET['fulltext']
    posts = Post.objects.filter(title__contains= entered_text).order_by('-created_at')

    return render(request, 'posts/result.html', {'posts':posts, 'alltext': entered_text})
