from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('level1.html', views.level1, name = "level1"),
    path('level2.html', views.level2, name = "level2"),
    path('level3.html', views.level3, name = "level3"),
    path('level4.html', views.level4, name = "level4"),
    path('level5.html', views.level5, name = "level5"),
    path('level6.html', views.level6, name = "level6"),
    path('congo.html', views.congo, name="congo"),
]
