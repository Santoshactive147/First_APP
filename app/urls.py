from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    
    path('home/', views.home,name="home" ),
    path("try/",views.try1,name="try1"),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:  # Only in development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)