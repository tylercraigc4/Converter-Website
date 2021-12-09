from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
#path('/converter',views.converter,name='converter'),
path('add',views.add, name='add'),
#path('test',views.tester, name= 'Test Me'),
#path('',include('converter.urls'))
path('testme/', views.TestMeView),
#path('converter', views.convert), 
path('', views.base),
]