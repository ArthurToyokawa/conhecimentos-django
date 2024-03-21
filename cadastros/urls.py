from django.urls import path
from .views import CreateEstudante, ListEstudante, UpdateEstudante, DeleteEstudante
# Importe suas views


urlpatterns = [
    path('estudante/create', CreateEstudante.as_view(), name='create-estudante'),
    path('estudante/update/<int:pk>', UpdateEstudante.as_view(), name='update-estudante'),
    path('estudante/delete/<int:pk>', DeleteEstudante.as_view(), name='delete-estudante'),
    path('estudante/', ListEstudante.as_view(), name='list-estudante'),
    
]
