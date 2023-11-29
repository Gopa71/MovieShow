from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def static(request):
  
    return render(request,'index.html')



# def demo(request):
  
#     return render(request,'index.html')
# def add(req):
#     x=int(req.GET['fno'])
#     y=int(req.GET['sno'])
#     res=x+y
#     return render(req,'add.html',{'res':res})
# def demo(request):
#     name='synafo'
#     return render(request,'index.html',{'name':name})

# def contact(request):
#     return render(request,'contact.html')

# def demo1(request):
#     return render(request,'demo1.html')

# def about(request):
#     return render(request,'about.html')

# def store(request):
#     return render(request,'store.html')