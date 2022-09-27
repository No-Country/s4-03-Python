from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import  messages
from django.views import generic
from django.urls import reverse_lazy
from . import views

# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request,user)
            messages.success(request,'Cuenta creada exitosamente')
            return redirect('home')
           

    return render(request,'useraccount/sign_up.html',{
        'form' : form,
    })
    