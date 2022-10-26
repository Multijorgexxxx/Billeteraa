from django.db import models
from django.contrib.auth.models import User
from adm.models import par_tipo_gastos, par_tipo_ganancias

# Create your models here.


class gastos(models.Model):
    ID = models.AutoField(primary_key=True)
    GASTO = models.CharField(max_length=100)
    COMENTARIO = models.TextField(blank=True)
    TIPO_GASTO = models.ForeignKey(par_tipo_gastos, on_delete=models.CASCADE)
    IMPORTANTE = models.BooleanField(default=False)
    VALOR = models.CharField(max_length=20)
    FECHA_CREACION = models.DateTimeField(auto_now_add=True)
    ESTADO = models.CharField(max_length=20, default=None)
    USUARIO = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.GASTO + ' - by ' + self.USUARIO.username


class ganancias(models.Model):
    ID = models.AutoField(primary_key=True)
    GANANCIA = models.CharField(max_length=100)
    COMENTARIO = models.TextField(blank=True)
    TIPO_GANANCIA = models.ForeignKey(
        par_tipo_gastos, on_delete=models.CASCADE)
    IMPORTANTE = models.BooleanField(default=False)
    VALOR = models.CharField(max_length=20)
    FECHA_CREACION = models.DateTimeField(auto_now_add=True)
    ESTADO = models.CharField(max_length=20, default=None)
    USUARIO = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.GANANCIA + ' - by ' + self.USUARIO.username
