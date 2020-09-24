from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.main, name='main'),
    path('landmark/', views.landmark, name='landmark'),
    path('landmark/<int:id>/', views.detail, name='detail'),
]