from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
from .forms import RegisterForm
from django.contrib import  messages
from django.views import generic
from django.urls import reverse_lazy
from . import views

# Create your views here.
def sign_up(request):
    if not request.user.is_authenticated:
        form = RegisterForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            user = form.save()
            if user:
                login(request,user)
                messages.success(request,'Cuenta creada exitosamente')
                return redirect('home')
        else:       
            return render(request,'useraccount/sign_up.html',{
                          'form' : form,
                        })
    else: 
        print("is_authenticated")
        return redirect('home')   

def logout_coffeelover(request):
    if not request.user.is_authenticated:
        return redirect('home')
    else:  
      logout(request)
      messages.success(request,'Salió de sesión exitosamente')
      return redirect('home')
        

def login_coffeelover(request):
    if request.user.is_authenticated:
        messages.error(request,'Ya estas logeado ')
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        
        if user:
            login(request,user)
            messages.success(request,'Bienvenido de nuevo {}'.format(user.username))
            return redirect('home')

        else:
            messages.error(request,'Usuario o contraseña no validos')
            
    return render(request,'useraccount/login.html', {})