from django.urls import path

#from converter import converter_app
from accounts import views as account_view
from converter_app import views as converter_view
from . import views

urlpatterns = [
    path('', account_view.login),
    path('register/', account_view.register, name='register'),
    path('testme/', converter_view.testme),
    path('home/', account_view.homePage, name='home'),
    path('converter/', converter_view.add, name='add'),
    path('login/', account_view.login),
    #path('logout/', account_view.logout)
    #path('converter/', views.converter)
    ]

