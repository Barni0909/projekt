from django.urls import path
from .views import index, feltoltes, feladat2, feladat3, feladat4, feladat5, feladat6, feladat7

urlpatterns = [
    path('', index),
    path('feltoltes/<str:table>', feltoltes),
    path('feladat/2', feladat2),
    path('feladat/3', feladat3),
    path('feladat/4', feladat4),
    path('feladat/5', feladat5),
    path('feladat/6', feladat6),
    path('feladat/7', feladat7),
]