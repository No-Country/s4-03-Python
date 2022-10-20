from django.shortcuts import render, redirect
from favorite.models import Favorite
from django.http import JsonResponse
from django.contrib.auth.models import User
from coffee_house.models import CoffeeHouse
from django.contrib import  messages
from django.db.models import Q
from django.urls import reverse_lazy, reverse
# Create your views here.

def delete_favorite(request, id):
    if not request.user.is_authenticated:
        messages.error(request,'Accion prohibida: No está autenticado')
        return redirect('home')
      
    house = CoffeeHouse.objects.get(id=id)
    name= User.objects.get(username=request.user.username)
    data_set = Favorite.objects.get(name=name, house=house, is_active=True)
    if data_set.delete():
        messages.success(request,'Felicidades, eliminaste la cafetería de favoritas')
    
    result_set = Favorite.objects.filter(name_id=name, is_active=True)
    context ={'coffees': result_set, 'detail_id': 9999 }
    return render(request, 'favorite/favorites_list.html',context)
  
  
    
def list(request, id):
    if not request.user.is_authenticated:
        messages.error(request,'Accion prohibida: No está autenticado')
        return redirect('home')
      
    name= User.objects.get(username=request.user.username) 
    result_set = Favorite.objects.filter(name_id=name, is_active=True)
    context ={'coffees': result_set, 'detail_id': 9999, 'via_detail': False }
    return render(request, 'favorite/favorites_list.html',context)
  
def add_favorites(request, id):
    if not request.user.is_authenticated:
        messages.error(request,'Accion prohibida: No está autenticado')
        return redirect('home')
    pk = request.user.id
    name= User.objects.get(username=request.user.username)
    house = CoffeeHouse.objects.get(id=id)
    already_exists = False
    if exists_cafeteria(name,house):
        data_set = Favorite.objects.filter(name=name)
        context = {'coffees':data_set, 'detail_id': id, 'via_detail': True}
        messages.error(request,'Acción incorrecta: Anteriormente ya había agregado a favoritos')     
        return render(request,'favorite/favorites_list.html', context)

    data_set = Favorite.objects.create(name=name, house=house, is_active=True) 
    data_set.save()
    data_set = Favorite.objects.filter(name=name)
    messages.success(request,'Felicidades, tienes una cafetería más en favoritas')
    context = {'coffees': data_set, 'detail_id': id, 'via_detail': True}
    return render(request,'favorite/favorites_list.html', context)

    '''
    if not exists_cafeteria(name,house):
        data_set = Favorite.objects.create(name=name, house=house, is_active=True) 
        data_set.save()
        already_exists = True
        data_set = Favorite.objects.filter(name=name)
        messages.success(request,'Felicidades, tienes una cafetería más en favoritas')
        context = {'coffees': data_set, 'detail_id': id, 'via_detail': True}
        return render(request,'favorite/favorites_list.html', context)
    else: 
        
      
    data_set = Favorite.objects.filter(name=name)
    context = {'coffees':data_set, 'detail_id': id, 'via_detail': True}
    return render(request,'favorite/favorites_list.html', context)

    '''
    
def favorite_fails(request):
    pass
def exists_cafeteria(user_name, house_name):
    return True if Favorite.objects.filter(name=user_name, house=house_name) else False
        
          