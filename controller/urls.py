from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    path('index/<str:pk>/', views.index, name='index'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutPage, name='logoutPage'),
    path('supplyCommand/', views.supplyCommand, name='supplyCommand'),
    path('exhaustCommand/', views.exhaustCommand, name='exhaustCommand'),
    path('offCommand/', views.offCommand, name='offCommand'),
    path('fanStatusCommand/', views.fanStatusCommand, name='fanStatusCommand'),
    path('semiOpenCommand/', views.semiOpenCommand, name='semiOpenCommand'),
    path('openCommand/', views.openCommand, name='openCommand'),
    path('closeCommand/', views.closeCommand, name='closeCommand'),
    path('ductStatusCommand/', views.ductStatusCommand, name='ductStatusCommand'),
    path('multipleSelect/', views.multipleSelect, name="multipleSelect"),
    path('fans/', views.fans, name='fans'),
    path('ducts/', views.ducts, name='ducts')
    # path('duct/', views.ductPage, name='ductPage'),
    # path('ac/', views.acPage, name='acPage'),
    # path('fans/', views.fans, name='fans'),
    # path('ducts/', views.ducts, name='ducts')
]
