from django.urls import path
from . import views
from django.contrib.auth import views as login_views

app_name = "accounts"

urlpatterns = [
    path('signup/',views.SignUp.as_view(), name="signup",kwargs={'hearde':'Sign Up Here'}),
    path('login/',login_views.LoginView.as_view(template_name = "accounts/login.html"),name="login", kwargs={'header':'Login'}),
    path('home/<username>',views.user_home_page,name="home"),
    path('home/',views.user_home_page,name="home"),
]
