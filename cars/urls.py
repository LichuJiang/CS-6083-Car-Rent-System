from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list_class, name='listclass'),
    path('register',views.register,name='register'),
    path('register/regisuccess',views.regisuccess,name='regisuccess'),
    path('login',views.login,name='login'),
    path('userplatform',views.userplatform,name='userplatform'),
    path('userplatform/search/',views.searchvehicle,name='searchvehicle'),
    path('userplatform/order/',views.ordervehicle,name='ordervehicle'),
    path('userplatform/myorder/',views.myorder,name='myorder'),
    path('userplatform/checkout/',views.checkout,name='checkout'),
    path('userplatform/payment/',views.payment,name='payment'),
    path('userplatform/paysuccess/',views.paysuccess,name='paysuccessful'),
    path('crud',views.vcrud,name='crud'),
    path('crud/addvehicle',views.addvehicle,name='addv'),
    path('crud/delvehicle/',views.delvehicle,name='delv')
]
#'/cars/userplatform/paysuccess'