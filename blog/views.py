from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

# Create your views here.
def index(request):
    """
    Show all the posts
    """
    posts = Post.objects.order_by('-created_at')[:6]
    template = loader.get_template('blog/index.html')
    context = {
        'title': 'Blog',
        'posts': posts
    }

    return HttpResponse(template.render(context, request))

def show(request, id):
    """
    Show a single post
    """
    post = Post.objects.filter(id=id)[0]
    template = loader.get_template('blog/show.html')
    context = {
        'title': post.title,
        'post': post
    }

    return HttpResponse(template.render(context, request))
