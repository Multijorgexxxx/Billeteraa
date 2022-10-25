from pyclbr import Class
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class par_tipo_gastos(models.Model):
    ID = models.AutoField(primary_key=True)
    DESCRIPCION = models.CharField(max_length=100)
    COMENTARIO = models.CharField(max_length=100)

    def __str__(self):
        return self.DESCRIPCION


class gastos(models.Model):
    ID = models.AutoField(primary_key=True)
    GASTO = models.CharField(max_length=100)
    COMENTARIO = models.TextField(blank=True)
    TIPO_GASTO = models.ForeignKey(par_tipo_gastos, on_delete=models.CASCADE)
    IMPORTANTE = models.BooleanField(default=False)
    VALOR = models.CharField(max_length=20)
    FECHA_CREACION = models.DateTimeField(auto_now_add=True)
    USUARIO = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.GASTO + ' - by ' + self.USUARIO.username
