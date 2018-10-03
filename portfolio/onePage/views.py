from django.shortcuts import render
from django.http import HttpRequest
from . import models
# Create your views here.
def index(request):
    return render(request,'onePage/index.html')

def getMemberId(request):
    