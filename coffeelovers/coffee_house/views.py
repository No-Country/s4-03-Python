from django.shortcuts import render
from .models import CoffeeHouse
# Create your views here.
def coffees_list(request):
    return render(request, 'coffee_house/coffees_list.html')

def coffee_detail(request, id):
    detail_result_set = CoffeeHouse.objects.filter(id=id)
    context = {'coffee_details': detail_result_set}
    return render(request, 'coffee_house/coffee_details.html',context)
       