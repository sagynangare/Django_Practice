from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="login/")

def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request,'personal/basic.html',{'content':['If you would like to contact me,please email me','sagy9975340919@gmail.com']})


def home(request):
    return render(request, "personal/home.html")
