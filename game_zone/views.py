from django.shortcuts import render
# from django.contrib.auth.views import ListView, DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request,"pages/index.html",{})


# class UserGameList(ListView,LoginRequiredMixin):
