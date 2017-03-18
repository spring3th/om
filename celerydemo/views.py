from django.shortcuts import render
from django.http import HttpResponse

from .tasks import hello_world

def index(request):
    hello_world.delay()
    return HttpResponse(u"Fuck th GFW!")

# Create your views here.
