from django.urls import path
from . import views

app_name = 'favorite'
urlpatterns=[
        path('list/', views.list,name='list'),
        path('add_favorites/<int:id>',views.add_favorites,name='add_favorites'),
    ]
