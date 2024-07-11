from django.shortcuts import render
from .models import Flan

# Create your views here.
def index(request):
    flans_pub = Flan.objects.filter(is_private = False)
    context = {
        'flans':flans_pub,
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def welcome(request):
    flans_priv = Flan.objects.filter(is_private = True)
    context = {
        'flans':flans_priv,
    }
    return render(request,'welcome.html',context)