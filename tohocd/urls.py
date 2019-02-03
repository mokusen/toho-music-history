from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('detail/', views.detail, name="detail"),
    path('cd/', views.cd, name="cd"),
    path('cd/detail/', views.cd_redirect, name="cd_detail"),
    path('cd/detail/<int:id>', views.cd_detail, name="cd_detail"),
    path('circle/', views.circle, name="circle"),
    path('vocal/', views.vocal, name="vocal"),
    path('vocal/detail/', views.vocal_redirect, name="vocal_detail"),
    path('vocal/detail/<int:id>', views.vocal_detail, name="vocal_detail"),
    path('lyric/', views.lyric, name="lyric"),
    path('lyric/detail/', views.lyric_redirect, name="lyric_detail"),
    path('lyric/detail/<int:id>', views.lyric_detail, name="lyric_detail"),
    path('arrange/', views.arrange, name="arrange"),
    path('arrange/detail/', views.arrange_redirect, name="arrange_detail"),
    path('arrange/detail/<int:id>', views.arrange_detail, name="arrange_detail"),
    path('orisong/', views.orisong, name="orisong"),
    path('orisong/detail/', views.orisong_redirect, name="orisong_detail"),
    path('orisong/detail/<int:id>', views.orisong_detail, name="orisong_detail"),
    path('oriwork/', views.oriwork, name="oriwork"),
    path('sitemap', views.sitemap, name='sitemap'),
]
