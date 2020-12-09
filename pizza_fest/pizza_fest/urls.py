"""pizza_fest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pizza.views import home,endForm,cadForm,pedidos,login,logout,ospedidos,pedidosFeitos

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
  path('admin/', admin.site.urls),
  path('home/', home, name="url_home"),
  path('logare/', endForm, name="url_logare"),
  path('logarc/', cadForm, name="url_logarc"),
  path('pedidos/', pedidos, name="url_pedidos"),
  path('login/', login, name="url_login"),
  path('logout/', logout, name="url_logout"),
  path('ospedidos/', ospedidos , name="url_ospedidos"),
  path('pedidosFeitos/', pedidosFeitos, name="url_feitos"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

