from django.urls import path
from .views import CreateEstudante, ListEstudante
# Importe suas views


urlpatterns = [
    path('estudante/novo', CreateEstudante.as_view(), name='create-estudante'),
    path('estudante/', ListEstudante.as_view(), name='list-estudante'),
    
]
