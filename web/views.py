from django.shortcuts import render
from .models import Flan, ContactForm
from .forms import ContactFormForm
from django.http import HttpResponseRedirect

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

def contactUs(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact = ContactForm(
                customer_email=form.cleaned_data['customer_email'],
                customer_name=form.cleaned_data['customer_name'],
                message=form.cleaned_data['message']
            )
            contact.save()
            return HttpResponseRedirect('/contact_success/')
    else:
        form = ContactFormForm()
    
    context = {
        'form': form
    }
    return render(request, 'contactUs.html', context)

def success(request):
    return render(request,'contact_success.html')
