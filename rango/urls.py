from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('achievements/', views.achievements, name = 'achievements'),
    path('play/', views.play, name = 'play'),
    path('play/dungeon/', views.dungeon, name = 'dungeon'),
    path('play/shop/', views.shop, name = 'shop'),
    path('play/stranger/', views.stranger, name = 'stranger'),
    path('play/shop/stats/', views.stats, name='stats_info'),
]