from django.shortcuts import render, get_object_or_404
from .models import Category, Post
# Create your views here.


def serve_html(request, path):
    return render(request, path)


def index(request, message=None):
    return render(request, 'index.html')


def post_list_view(request, category=None):
    if category:
        if category == 'all':
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(category__name=category)
    else:
        posts = Post.objects.filter(category=None)

    data = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context=data,)


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context=data)
