from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import Estagio, Estudante
from django.urls import reverse_lazy

class ListEstudante(ListView):
    model = Estudante
    template_name = 'cadastros/list_estudante.html'

class CreateEstudante(CreateView):
    model = Estudante
    fields = ['nome', 'matricula', 'email', 'data_nascimento']
    template_name = 'cadastros/form_create.html'
    success_url = reverse_lazy('list-estudante')

class UpdateEstudante(UpdateView):
    model = Estudante
    fields = ['nome', 'matricula', 'email', 'data_nascimento']
    template_name = 'cadastros/form_create.html'
    success_url = reverse_lazy('list-estudante')


class DeleteEstudante(DeleteView):
    model = Estudante
    template_name = 'cadastros/form_delete.html'
    success_url = reverse_lazy('list-estudante')


# Create your views here.
