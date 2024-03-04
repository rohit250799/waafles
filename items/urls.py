from django.urls import path
from . import views
#import views

app_name = 'items'

urlpatterns = [
    path('', views.itemsIndex, name='index'),
    path('new/', views.newitem, name='newitem'),
    path('<int:pk>/edit/', views.edititem, name='edititem'),
]
