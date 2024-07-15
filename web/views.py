from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormModelForm, SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
    flans_pub = Flan.objects.filter(is_private = False)
    context = {
        'flans':flans_pub,
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

@login_required
def welcome(request):
    flans_priv = Flan.objects.filter(is_private = True)
    context = {
        'flans':flans_priv,
    }
    return render(request,'welcome.html',context)

def contactUs(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact_success/')
    else:
        if request.user.is_authenticated:
            initial_data = {
                'customer_email': request.user.email,
                'customer_name': request.user.get_full_name()
            }
            form = ContactFormModelForm(initial=initial_data)
        else:
            form = ContactFormModelForm()

    context = {
        'form': form
    }
    return render(request, 'contactUs.html', context)

def success(request):
    return render(request,'contact_success.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Usuario registrado correctamente.')
            return redirect('bienvenido')
        else:
            print(form.errors)
    else:
        form = SignUpForm()

    context = {
        'form' : form,
    }

    return render(request, 'signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'Has iniciado sesión correctamente.')
                return redirect('bienvenido')
                
    else:
        form = AuthenticationForm()

    context = {
        'form':form,
    }

    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('index')

@login_required
def update_account(request):
    if request.method == 'POST':
        user = request.user
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
        if new_first_name:
            user.first_name = new_first_name
        if new_last_name:
            user.last_name = new_last_name
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password:
            if current_password:
                if user.check_password(current_password):
                    if new_password == confirm_password:
                        user.set_password(new_password)
                        user.save()
                        update_session_auth_hash(request, user)
                        messages.success(request, 'Tus datos han sido actualizados y la contraseña cambiada correctamente.')
                    else:
                        messages.error(request, 'Las nuevas contraseñas no coinciden.')
                else:
                    messages.error(request, 'La contraseña actual es incorrecta.')
            else:
                messages.error(request, 'Debes proporcionar tu contraseña actual para cambiar la contraseña nueva.')

        user.save()
        messages.success(request, 'Tus datos han sido actualizados correctamente.')
        return redirect('bienvenido')

    return render(request, 'welcome.html')
