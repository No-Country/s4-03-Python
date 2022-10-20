from django.urls import path
from . import views

app_name = 'favorite'
urlpatterns=[
        path('list/<int:id>', views.list,name='list'),
        path('add_favorites/<int:id>',views.add_favorites,name='add_favorites'),
        path('delete_favorite/<int:id>',views.delete_favorite,name='delete_favorite'),
    ]
