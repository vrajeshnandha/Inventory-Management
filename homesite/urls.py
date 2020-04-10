from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viewstock', views.viewStock, name='viewstock'),
    path('addstock', views.addStock, name='addstock'),
    path('viewentry', views.viewEntry, name='viewentry'),
    path('deleteentry', views.deleteEntry, name='deleteentry'),
    path('worker', views.worker, name='worker'),
    path('payment', views.payment, name='payment'),
]
