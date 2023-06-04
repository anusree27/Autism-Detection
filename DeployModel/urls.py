
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views
from userlog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('home/', views.home ,name="home"),
    path('result/',views.result,name="result"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
]
