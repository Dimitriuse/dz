from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def top(request):
    return render(request,'top-sellers.html')

def login(request):
    return render(request,'login.html')

def reg(request):
    return render(request,'register.html')

def profile(request):
    return render(request,'profile.html')

def add_post(request):
    return render(request,'advertisement-post.html')