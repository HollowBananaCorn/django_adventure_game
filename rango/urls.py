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
    path('play/stranger/boss_area/', views.bossArea, name = 'boss_area'),
    path('play/stranger/boss_area/boss_talk', views.bossTalk, name = 'boss_talk'),
    path('play/stranger/boss_area/boss_talk/boss', views.boss, name = 'boss'),
    path('play/shop/stats/', views.stats, name='stats_info'),
    path('updated_play/', views.updatedPlay, name='updated_play'),
    path('update_score/', views.update_score, name='update_score'),

    path('update_health/', views.update_health, name='update_health'),
    path('update_gold/', views.update_gold, name='update_gold'),
    path('update_attack/', views.update_attack, name='update_attack'),
    path('update_defense/', views.update_defense, name='update_defense'),
    path('update_agility/', views.update_agility, name='update_agility'),
    path('delete_character/', views.delete_character, name ='delete_character')
]