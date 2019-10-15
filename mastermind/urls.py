from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
app_name = "mastermind"

urlpatterns = [
    path('',login_required(views.HomePage.as_view()),name="playmastermind"),
]
