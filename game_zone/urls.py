"""game_zone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sudoku import views as s_views
from accounts import views as ac_views
from game_zone import views
from django.contrib.auth import views as login_views



urlpatterns = [
    path('',views.index, name = "index"),
    path('sudoku/',include("sudoku.urls", namespace="sudoku"),name="playsudoku"),
    path('accounts/', include("accounts.urls"),name="signup"),
    path('mastermind/',include("mastermind.urls"), name="mastermind"),
    path('home/',ac_views.user_home_page,name="home"),
    path('logout/',login_views.LogoutView.as_view(), name="logout"),
    path('admin/', admin.site.urls),
]
