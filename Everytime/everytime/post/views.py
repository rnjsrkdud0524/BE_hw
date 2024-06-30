from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'post/list.html', {'posts' : posts})

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymity')
        author = request.user
        
        anonymity = anonymity == "on"
        Post.objects.create(
                title = title,
                content = content,
                anonymity = anonymity,
                author = author
            )
        return redirect('post:create')
    return render(request, 'post/create.html')

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'post/detail.html', {'post' : post})

@login_required
def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        if video:
            post.video.delete()
            post.video = video
        if image:
            post.image.delete()
            post.image = image

        post.save()
        return redirect('post:detail', id)
    return render(request, 'post/update.html', {'post' : post})

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('post:list')

@login_required
def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymity') == "on"  

        Comment.objects.create(
            post=post,
            content=content,
            user=request.user,
            anonymity=anonymity
        )
        return redirect('post:detail', id=post_id)  
    return redirect('post:detail', id=post_id)

@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    comment.delete()
    return redirect('post:detail', post_id)

@login_required
def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.add(request.user)
    return redirect('post:detail', post_id)

@login_required
def remove_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.remove(request.user)
    return redirect('post:detail', post_id)

@login_required
def add_scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.scrap.add(request.user)
    return redirect('post:detail', post_id)

@login_required
def remove_scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.scrap.remove(request.user)
    return redirect('post:detail', post_id)