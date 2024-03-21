from django.urls import path
from .views import LoginUser, LogoutUser
# Importe suas views


urlpatterns = [
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),
    # path('estudante/update/<int:pk>',
    #      UpdateEstudante.as_view(), name='update-estudante'),
    # path('estudante/delete/<int:pk>',
    #      DeleteEstudante.as_view(), name='delete-estudante'),
    # path('estudante/', ListEstudante.as_view(), name='list-estudante'),

]
