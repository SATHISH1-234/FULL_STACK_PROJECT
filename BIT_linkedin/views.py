from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def mynet(request):
    return render(request,'mynet.html')

def login(request):
    return render(request,'login.html')

def resume(request):
    return render(request,'resume.html')

def register(request):
    return render(request,'register.html')

def jobs(request):
    return render(request,'jobs.html')

def message(request):
    return render(request,'messaging.html')

def notify(request):
    return render(request,'notify.html')