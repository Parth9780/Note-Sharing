from django.contrib import admin
from django.urls import path,include
from hexaapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('products/',views.products,name='products'),
    path('single_product/',views.single_product,name='single_product'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'), 
    
]