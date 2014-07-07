from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def home(request):
    current_date = datetime.datetime.now()
    return render_to_response('itms/home.html', locals())

def login(request):
    current_date = datetime.datetime.now()
    return render_to_response('itms/login.html', locals())
