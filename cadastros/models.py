from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.nome}/{self.estado}"
    
    class Meta:
        ordering = ["nome", "estado"]
        
class Estudante(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()
    atualizado_em = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nome
    

class Estagio(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.PROTECT)
    empresa = models.CharField(max_length=255)
    data_inicio = models.DateField(verbose_name="Data de início")
    data_termino = models.DateField(blank=True)
    carga_horaria = models.IntegerField()
    # protocolado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    data_protocolo: models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}/{self.empresa}"

    