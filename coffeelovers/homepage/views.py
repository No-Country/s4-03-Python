from django.shortcuts import render
from coffee_house.models import CoffeeHouse
from app_config.models import TitleMessage
from django.contrib import  messages
from django.db.models import Q
from random import randint


# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    coffees = list(CoffeeHouse.objects.filter(
                  Q(name__icontains=q) |
                  Q(city__icontains=q) |
                  Q(address__icontains=q)
                  ).values('name','coffee_image','stars_average','city','id').order_by('-stars_average')[:8])
      
    if not(len(coffees)):
        messages.error(request,'No se encontró cafetería con esos criterios')
        
    coffee_images_list = stars_ranked()
    if len(coffees) > 0 and len(coffees) !=8:
        card1 = coffees[0]
        card1_found= {'card1_selected': True }
    else:
        card1= coffee_images_list[0]  
        card1_found= {'card1_selected': False }    
        
    if len(coffees) > 1 and len(coffees)!=8:
        card2 = coffees[1]
        card2_found= {'card2_selected': True }
    else:
        card2= coffee_images_list[1]  
        card2_found= {'card2_selected': False }  
    
    if len(coffees) > 2 and len(coffees)!=8:
        card3 = coffees[2]
        card3_found= {'card3_selected': True }
    else:
        card3= coffee_images_list[2]  
        card3_found= {'card3_selected': False }  
    
    if len(coffees) > 3 and len(coffees)!=8:
        card4 = coffees[3]
        card4_found= {'card4_selected': True }
    else:
        card4= coffee_images_list[3]  
        card4_found= {'card4_selected': False }  
    
    if len(coffees) > 4 and len(coffees)!=8:
        card5 = coffees[4]
        card5_found= {'card5_selected': True }
    else:
        card5= coffee_images_list[4]  
        card5_found= {'card5_selected': False }  
    
    if len(coffees) > 5 and len(coffees)!=8:
        card6 = coffees[5]
        card6_found= {'card6_selected': True }
    else:
        card6= coffee_images_list[5]  
        card6_found= {'card6_selected': False }  
    
    if len(coffees) > 6 and len(coffees)!=8:
        card7 = coffees[6]
        card7_found= {'card7_selected': True }
    else:
        card7= coffee_images_list[6]  
        card7_found= {'card7_selected': False }  
    
    if len(coffees) > 7 and len(coffees)!=8:
        card8 = coffees[7]
        card8_found= {'card8_selected': True }
    else:
        card8= coffee_images_list[7]  
        card8_found= {'card8_selected': False }  
    
    context = {'coffee_title': selected_title(),
               'card1': card1,
               'card2': card2,
               'card3': card3,
               'card4': card4,
               'card5': card5,
               'card6': card6,
               'card7': card7,
               'card8': card8,
               'card1_found': card1_found,
               'card2_found': card2_found,
               'card3_found': card3_found,
               'card4_found': card4_found,
               'card5_found': card5_found,
               'card6_found': card6_found,
               'card7_found': card7_found,
               'card8_found': card8_found,
              }
    return render(request, 'homepage/home.html', context)

def stars_ranked():
    stars_best_ranked_set= list(CoffeeHouse.objects.filter().values('name','coffee_image','stars_average','city','id').order_by('-stars_average')[:8])
    return stars_best_ranked_set

def selected_title():
    titles_result_set = TitleMessage.objects.filter(is_active=True).values('title') 
    record_selected = randint(0,len(titles_result_set)-1)  
    return titles_result_set[record_selected]