from django.shortcuts import render, redirect
from favorite.models import Favorite
from django.http import JsonResponse
from django.contrib.auth.models import User
from coffee_house.models import CoffeeHouse
from django.contrib import  messages
from django.db.models import Q
from django.urls import reverse_lazy, reverse
# Create your views here.

def list(request, id):
    if not request.user.is_authenticated:
        messages.error(request,'Accion prohibida: No está autenticado')
        return redirect('home')
    id = request.detail_id
    print("THE DETAILS: {}".format(id))
    pk = request.user.id
    name= User.objects.get(username=request.user.username) 
    result_set = Favorite.objects.filter(name_id=name)
        
    context ={'coffees': result_set, 'detail_id':id}
    print("Result:{}".format(result_set))
    return render(request, 'favorite/favorites_list.html',context)

def add_favorites(request, id):
    if not request.user.is_authenticated:
        messages.error(request,'Accion prohibida: No está autenticado')
        return redirect('home')
    pk = request.user.id
    name= User.objects.get(username=request.user.username)
    house = CoffeeHouse.objects.get(id=id)
    if not exists_cafeteria(name,house):
        data_set = Favorite.objects.create(name=name, house=house) 
        data_set.save()
        data_set = Favorite.objects.filter(name=name)
        messages.success(request,'Felicidades, tienes una cafetería más en favoritas')
        context = {'coffees': data_set, 'detail_id': id}
        return render(request,'favorite/favorites_list.html', context)
    
    messages.error(request,'Acción incorrecta: Anteriormente ya había agregado a favoritos') 
    data_set = Favorite.objects.filter(name=name)
    context = {'coffees': data_set, 'detail_id': id}
    return render(request,'favorite/favorites_list.html', context)

def exists_cafeteria(user_name, house_name):
    return True if Favorite.objects.filter(name=user_name, house=house_name) else False
        
          