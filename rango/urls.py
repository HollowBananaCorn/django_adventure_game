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
    path('play/dungeon1/', views.dungeon1, name = 'dungeon1'),
    path('updated_play/updated_dungeon1/', views.updated_dungeon1, name = 'updated_dungeon1'),
    path('play/dungeon2/', views.dungeon2, name = 'dungeon2'),
    path('updated_play/updated_dungeon2/', views.updated_dungeon2, name = 'updated_dungeon2'),
    path('play/dungeon3/', views.dungeon3, name = 'dungeon3'),
    path('updated_play/updated_dungeon3/', views.updated_dungeon3, name = 'updated_dungeon3'),
    path('play/shop/', views.shop, name = 'shop'),
    path('play/stranger/', views.stranger, name = 'stranger'),
    path('play/stranger/boss_area/', views.bossArea, name = 'boss_area'),
    path('play/stranger/boss_area/boss_talk', views.bossTalk, name = 'boss_talk'),
    path('play/stranger/boss_area/boss_talk/boss', views.boss, name = 'boss'),
    path('play/shop/stats/', views.stats, name='stats_info'),
    path('updated_play/', views.updatedPlay, name='updated_play'),
    path('updated_play/updated_shop', views.updatedShop, name='updated_shop'),
    path('updated_play/updated_shop/updated_stats', views.updatedStats, name='updated_stats_info'),

    path('update_health/', views.update_health, name='update_health'),
    path('update_gold/', views.update_gold, name='update_gold'),
    path('delete_character/', views.delete_character, name ='delete_character')
]