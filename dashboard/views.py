#coding=utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import *
import logging


logger = logging.getLogger('django')

@login_required(login_url="/account/login/")
def index(request):




    return render(request, 'dashboard/index.html', {})
