from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viewstock', views.viewStock, name='viewstock'),
    path('addstock', views.addStock, name='addstock'),
    path('view', views.view, name='view'),
]