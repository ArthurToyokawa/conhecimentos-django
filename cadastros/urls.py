from django.urls import path
from .views import CreateEstudante, ListEstudante, UpdateEstudante, DeleteEstudante, CreateEstagio, ListEstagio, UpdateEstagio, DeleteEstagio
# Importe suas views


urlpatterns = [
    path('estudante/create', CreateEstudante.as_view(), name='create-estudante'),
    path('estudante/update/<int:pk>', UpdateEstudante.as_view(), name='update-estudante'),
    path('estudante/delete/<int:pk>', DeleteEstudante.as_view(), name='delete-estudante'),
    path('estudante/', ListEstudante.as_view(), name='list-estudante'),
    path('estagio/create', CreateEstagio.as_view(), name='create-estagio'),
    path('estagio/update/<int:pk>', UpdateEstagio.as_view(), name='update-estagio'),
    path('estagio/delete/<int:pk>', DeleteEstagio.as_view(), name='delete-estagio'),
    path('estagio/', ListEstagio.as_view(), name='list-estagio'),
    
]
