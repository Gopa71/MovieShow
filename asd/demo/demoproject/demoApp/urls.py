
from django.urls import path
from .import views
urlpatterns = [
    path('',views.static,name='static')
    # path('',views.demo,name='demo'),
    # path('add/',views.add,name='add')
    # path('contact/',views.contact,name='contact'),
    # path('demo1/',views.demo1,name='demo1'),
    # path('about/',views.about,name='about'),
    # path('store/',views.store,name='store')
]