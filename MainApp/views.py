from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from blog.models import HomeInfo

# Create your views here.
def Home(request):
    info = HomeInfo.objects.first()
    context ={
        'info' : info
    }
    return render(request,'home.html',context)