from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.home_redirect, name='home_redirect'),
    path('', views.index, name='home'),
    path('office/<int:id>', views.office, name='office'),
    path('driver/', views.driver, name='driver'),
    path('save-location/', views.location_save, name='location_save'),

    
]