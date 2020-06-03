from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('map', views.mapCoordinates),
    path('heat', views.heatmap)
]
