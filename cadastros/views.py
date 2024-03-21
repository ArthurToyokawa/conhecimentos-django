from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import Estagio, Estudante
from django.urls import reverse_lazy


class CreateEstudante(CreateView):
    model = Estudante
    fields = ['nome', 'matricula', 'email', 'data_nascimento']
    template_name = 'cadastros/form_create.html'
    success_url = reverse_lazy('index')

class ListEstudante(ListView):
    model = Estudante
    template_name = 'cadastros/list_estudante.html'

# Create your views here.
