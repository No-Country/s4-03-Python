from django.urls import path, include

from . import views
app_name = 'useraccount'
urlpatterns = [
    path('sign_up',views.sign_up,name='sign_up'),
    path('logout',views.logout_coffeelover,name='logout'),
    path('login',views.login_coffeelover, name='login'),
 
]