from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from django.template import loader

from .models import Payment

# Create your views here.
def index(request):
    """
    List all the payments
    """
    paymetns = Payment.objects.order_by('-created_at')[:12]
    template = loader.get_template('payments/index.html')
    context = {
        'title': 'Payments',
        'payments': payments
    }

    return HttpResponse(template.render(context, request))

def show(request, id):
    """
    Show a single post
    """
    post = Post.objects.filter(id=id)[0]
    template = loader.get_template('blog/show.html')
    context = {
        'title': payment.name,
        'payment': payment
    }

    return HttpResponse(template.render(context, request))
=======

# Create your views here.
>>>>>>> 0339e0b2d7926a4ccd9a41d3774e65167d35ada5
