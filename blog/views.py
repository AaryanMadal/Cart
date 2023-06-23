from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *

# Create your views here.
def index(request):
    blogs=Blogpost.objects.all()

    return render(request,'blog/index.html',{'blogs':blogs})

def blogpost(request,id):
    post=Blogpost.objects.filter(post_id=id)[0]
    blogs=Blogpost.objects.all()
    pr=False
    nx=False
    left=Blogpost.objects.filter(post_id=id-1)
    if len(left)>0:
        pr=True
    right=Blogpost.objects.filter(post_id=id+1)
    if len(right)>0:
        nx=True

    return render(request,'blog/blogpost.html',{'post':post,'pr':pr,'nx':nx,'left':left,'right':right})