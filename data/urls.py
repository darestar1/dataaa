"""
URL configuration for data project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
   
    path('observations/create/', views.observation_create, name='observation_create'),
    path('observations/', views.observation_list, name='observation_list'),
    

    
    path('observations/update/<int:observation_id>/', views.observation_update, name='observation_update'),


    path('observations/update/', views.observation_list, name='observation_list'),
    path('observations/list/readonly/', views.observation_list_readonly, name='observation_list_readonly'),

    path('observations/delete/', views.delete_observation, name='delete_observation'),
    path('rocks/', views.rock_list, name='rock_list'),
    path('rocks/create/', views.rock_create, name='rock_create'),
    path('rocks/update/<int:rock_id>/', views.rock_update, name='rock_update'),
    path('rocks/delete/', views.delete_rock, name='rock_delete'),
    path('rocks/update/', views.rock_list, name='rock_list'),
    
    
    path('rocks/list/readonly/', views.rock_list_read, name='rock_list_read'),
    path('streams/', views.stream_list, name='stream_list'),
    path('streams/create/', views.stream_create, name='stream_create'),
    path('streams/update/<int:stream_id>/', views.stream_update, name='stream_update'),
    path('streams/delete/', views.delete_stream, name='stream_delete'),
    path('streams/update/', views.stream_list, name='stream_list'),

    path('streams/list/readonly/', views.stream_list_read, name='stream_list_read'),
    path('soils/', views.soil_list, name='soil_list'),
    path('soils/create/', views.soil_create, name='soil_create'),
    path('soils/update/<int:soil_id>/', views.soil_update, name='soil_update'),
    path('soils/delete/', views.soil_delete, name='soil_delete'),
    path('soils/update/', views.soil_list, name='soil_list'),

    path('soils/list/readonly/', views.soil_list_read, name='soil_list_read'),
    path('oremicroscopies/', views.ore_microscopy_list, name='ore_microscopy_list'),
    path('oremicroscopies/create/', views.ore_microscopy_create, name='ore_microscopy_create'),
    path('oremicroscopies/update/<int:ore_microscopy_id>/', views.ore_microscopy_update, name='ore_microscopy_update'),
    path('oremicroscopies/delete/', views.ore_microscopy_delete, name='ore_microscopy_delete'),
    path('oremicroscopies/update/', views.ore_microscopy_list, name='ore_microscopy_list'),
    
    path('oremicroscopies/list/readonly/', views.ore_microscopy_list_read, name='ore_microscopy_list_read'),

]
