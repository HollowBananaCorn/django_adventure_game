from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('achievements/', views.achievements, name = 'achievements'),
    path('play/', views.play, name = 'play'),
]