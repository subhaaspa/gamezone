from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePage(TemplateView,LoginRequiredMixin):
    template_name = "mastermind/play_mastermind.html"
