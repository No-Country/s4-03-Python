from django.urls import path
from coffee_house.views import coffees_list
from coffee_house.views import coffee_detail
from . import views
app_name = 'coffee_house'
urlpatterns = [
    path('', coffees_list, name='coffees_list'),
    path('details/<int:id>', coffee_detail,name='details'),
]