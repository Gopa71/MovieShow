from django.shortcuts import render

# Create your views here.

def static(req):
  return render(req,'index.html')

def contact(req1):
  return render(req1,'contact.html')

def destinations(req2):
  return render(req2,'destinations.html')

def elements(req3):
  return render(req3,'elements.html')

def news(req4):
  return render(req4,'news.html')