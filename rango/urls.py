from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),

    path('achievements/', views.achievements, name = 'achievements'),
    path('play/', views.play, name = 'play'),
    path('play/dungeon/', views.dungeon, name = 'dungeon'),
    path('play/shop/', views.shop, name = 'shop'),
    path('play/stranger/', views.stranger, name = 'stranger'),
    path('play/shop/stats/', views.stats, name='stats_info'),
]