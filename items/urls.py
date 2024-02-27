from django.urls import path
from . import views
#import views

app_name = 'items'

urlpatterns = [
    #path('items/', views.itemsTest, name='items'),
    path('', views.itemsTest, name='items'),
    path('new/', views.newitem, name='newitem'),
]
