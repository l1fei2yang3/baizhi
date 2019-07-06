from django.urls import path

from bai import views

app_name='baiapp'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('introduce/',views.introduce,name='introduce'),
    path('menu/',views.menu,name='menu'),
    path('mainc/',views.mainc,name='mainc'),
    path('login/',views.login,name='login'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('register/',views.register,name='register'),
    path('registerlogic/',views.registerlogic,name='registerlogic'),
    path('checkName/',views.checkName,name='checkName'),
    path('huakuai/',views.huakuai,name='huakuai'),
]