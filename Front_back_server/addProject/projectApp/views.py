from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request,'index.html')
def add(req):
    x=int(req.GET['fno'])
    y=int(req.GET['sno'])
    res=x+y
    return render(req,'add.html',{'res',res})