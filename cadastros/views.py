from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class UpdateEstudante(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Estudante
    fields = ['nome', 'matricula', 'email', 'data_nascimento']
    template_name = 'cadastros/form_create.html'
    success_url = reverse_lazy('list-estudante')
    login_url = reverse_lazy('login')
    permission_required = u"Administrador"


class DeleteEstudante(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Estudante
    template_name = 'cadastros/form_delete.html'
    success_url = reverse_lazy('list-estudante')
    login_url = reverse_lazy('login')
    permission_required = u"Administrador"
    

class ListEstagio(ListView):
    model = Estagio
    template_name = 'cadastros/list_estagio.html'


class CreateEstagio(CreateView):
    model = Estagio
    fields = ['estudante', 'empresa', 'data_inicio', 'data_termino', 'carga_horaria']
    template_name = 'cadastros/form_create.html'
    success_url = reverse_lazy('list-estagio')


class UpdateEstagio(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Estagio
    fields = ['estudante', 'empresa', 'carga_horaria', 'data_termino']
    template_name = 'cadastros/form_create.html'
    success_url = reverse_lazy('list-estagio')


class DeleteEstagio(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Estagio
    template_name = 'cadastros/form_delete.html'
    success_url = reverse_lazy('list-estagio')
    login_url = reverse_lazy('login')
    permission_required = u"Administrador"


# Create your views here.
