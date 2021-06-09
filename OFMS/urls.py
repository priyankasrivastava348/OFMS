"""OFMS URL Configuration

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
from django.urls import path
from Home . views import homefun
from Login . views import loginfun ,dashboard, logoutfun 
from Signup . views import signupfun, signupsavefun
from service . views import gethotels , getitems , placeorder, orderstatus  , getorderstatus , updateorderstatus 
from Hotel . views import getorderslist
from contact.views import contactfun
from delivery . views import dborders , dbupdateorderstatus, checkneworder , dbgetorder

# in our project 3 types of user 
# hotel manage as user 
# delivery boy as user 
# client user 

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', homefun , name = 'home'), 
    path ('login/', loginfun, name = 'login' ),
    path ('signup/', signupfun , name = 'signup'),
    path ('signup/save/', signupsavefun ) , 
    path ('dashboard/',dashboard, name = 'dashboard'), 
    path ('logout/', logoutfun ), 
    path ('hotels/', gethotels ), 
    path ('hotels/<int:hid>/orders/<int:oid>/update/', updateorderstatus ) , 
    path ('hotels/<int:id>/', getitems ), 
    path ('hotels/<int:id>/orders/', getorderslist , name = 'getorderslist'), # this url is dedicated for hotel manager
    path ('placeorder/', placeorder , name = 'placeorder'),
    path ('orderstatus/<int:id>/', orderstatus , name = 'orderstatus'),
    path ('contact/',contactfun),
    path ('getorderstatus/<int:id>/', getorderstatus , name = 'getorderstatus' ), 
    path ( 'delivaryboy/<int:id>/', dborders , name = 'dborders'),
    path ('deliveryboy/<int:dvid>/<int:oid>/update/', dbupdateorderstatus),
    path ('delivaryboy/<int:dvid>/<int:oid>/getorder/', dbgetorder),
    path ( 'checkneworder/', checkneworder , name = 'checkneworder')
]
