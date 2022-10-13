
from django.contrib import admin
from django.urls import path, include
from homepage import urls
from useraccount import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('useraccount/', include('useraccount.urls')),
    path('coffee_house/', include('coffee_house.urls')),
    path('app_config/',include('app_config.urls')),
    path('favorite/',include('favorite.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
