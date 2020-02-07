"""codemonk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from food_plaza import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),
    path('about', views.about),
    path('registration',views.registration),
    path('login',views.login),
    path('verify',views.login_verify),
    path('addData',views.addData),
    path('addrecipe',views.addrecipe),
    path('viewrecipe',views.view_recipe),
    path('filter',views.filter),
    path('editrecipe',views.editrecipe),
   
    path('view/<item>/',views.view_recipe),
    path('editing_recipe',views.editing),
    
]



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)



