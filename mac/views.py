
from django.shortcuts import render
from django.http import HttpResponse
from math import *
# Create your views here.
def index(request):
        return render(request,'index.html')