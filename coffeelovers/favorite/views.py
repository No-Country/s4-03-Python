from django.shortcuts import render, redirect
from favorite.models import Favorite
from django.http import JsonResponse
from django.contrib import  messages
from django.db.models import Q
# Create your views here.

def favorites(request):
    context = {'context': 'Hello from favorites view'}
    return render(request, 'favorites.html', context)

def favorite_list(request, id ):
    if not user.is_authenticated():
        messages.error(request,'Accion prohibida: No está autenticado')
        return redirect('home')
    
    return render(request, 'favorite/favorite_list.html', context)