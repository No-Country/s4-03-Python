
from django.contrib import admin
from django.urls import path, include
from homepage import urls
from useraccount import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('useraccount/', include('useraccount.urls')),
]
