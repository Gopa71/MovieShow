from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')
def movie1(req):
    return render(req,'movie1.html')
def movie2(req):
    return render(req,'movie2.html')