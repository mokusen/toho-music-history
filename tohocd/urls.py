from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('detail/', views.detail, name="detail"),
    path('cd/', views.cd, name="cd"),
    path('circle/', views.circle, name="circle"),
    path('vocal/', views.vocal, name="vocal"),
    path('lyric/', views.lyric, name="lyric"),
    path('arrange/', views.arrange, name="arrange"),
    path('orisong/', views.orisong, name="orisong"),
    path('oriwork/', views.oriwork, name="oriwork"),
]