
from django.contrib import admin
from django.urls import path, include
from homepage import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls'))
]
