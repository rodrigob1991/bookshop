"""libreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lib import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^libro/(?P<numero_libro>[0-9]+)/', views.prestar_libro,name="prestar_libro"),
    url(r'^libros_prestados/',views.libros_prestados,name="libros_prestados"),
    url(r'^$',views.libros_disponibles,name="libros_disponibles"),
    
    
    	
]
