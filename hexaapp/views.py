from django.shortcuts import render,redirect
from .forms import *
from .models import *
import requests
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def products(request):
    return render(request,'products.html')

def single_product(request):
    return render(request,'single-product.html')

def signin(request):
    if request.method=='POST':
        unm=request.POST['email']
        pas=request.POST['password']
        
        user1=hexauser.objects.filter(email=unm,password=pas)
        uid=hexauser.objects.get(email=unm)
        if user1:
            print("Login successfully!")
            request.session['user1']=unm
            return redirect('index')
    return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        newuser=user_signup(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User is succefuly add")
            # return redirect('signin')
            
        else:
            print("User is not add")
    
    # global otp
    # otp=random.randint(1111,9999)
    # url = "https://www.fast2sms.com/dev/bulkV2"
    # querystring = {"authorization":"gWMAeKq0ExoPnDvUiHGbj1OJsF9aC8yB7dR6L254hVcXrfNmQTc1NKT34eJrdkRYMFqlHwSsLAfmCZ70","variables_values":f"{otp}","route":"otp","numbers":f"{request.POST['mobile']}"}
    # headers = {
    #     'cache-control': "no-cache"
    #     }
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    return render(request,'signup.html')

