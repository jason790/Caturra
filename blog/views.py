from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created_at')[:6]
    template = loader.get_template('blog/index.html')
    context = {
        'title': 'Posts',
        'posts': posts
    }
    return HttpResponse(template.render(context, request))
