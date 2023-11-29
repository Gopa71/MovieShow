
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('movie1/',views.movie1,name='movie1'),
    path('',views.movie2,name='movie2'),

   
]