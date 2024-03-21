from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy


class LoginUser(LoginView):
    model = User
    fields = ['username', 'password']
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('index')
    


class LogoutUser(LogoutView):
    extra_context = {'titulo': 'Logout'}


# Create your views here.
