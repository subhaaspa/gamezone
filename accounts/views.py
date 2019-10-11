from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from accounts import forms
from django.views.generic import CreateView
# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'



def user_home_page(request,username=""):
    return render(request,"pages/index.html" ,{'user':username})
