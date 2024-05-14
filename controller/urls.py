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
    path('ducts/', views.ducts, name='ducts'),
    # path('ductsPosition/', views.ductsPosition, name='ductsPosition'),
    # path('ductPositionUpdate/<str:btnID>/<int:value>', views.ductPositionUpdate, name='ductPositionUpdate'),
    # path('duct/', views.ductPage, name='ductPage'),
    # path('ac/', views.acPage, name='acPage'),
    # path('fans/', views.fans, name='fans'),
    # path('ducts/', views.ducts, name='ducts')
    path('createMode/', views.createMode, name='createMode'),
    path('addMode/', views.addMode, name='addMode'),
    path('getModes', views.getModes, name='getModes'),
    path('executeMode', views.executeMode, name='executeMode'),
    path('deleteMode', views.deleteMode, name='deleteMode'),
    path('ductsPosition', views.ductsPosition, name='ductsPosition'),
    path('ductPositionUpdate/', views.ductPositionUpdate, name='ductPositionUpdate'),
    path('getDuctMaxValue/', views.getDuctMaxValue, name='getDuctMaxValue'),
]
