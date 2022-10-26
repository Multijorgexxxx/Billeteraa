from django.db import models

# Create your models here.


class par_tipo_gastos(models.Model):
    ID = models.AutoField(primary_key=True)
    DESCRIPCION = models.CharField(max_length=100)
    COMENTARIO = models.CharField(max_length=100)
    TIPO = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.DESCRIPCION + '-' + self.TIPO


class par_tipo_ganancias(models.Model):
    ID = models.AutoField(primary_key=True)
    DESCRIPCION = models.CharField(max_length=100)
    COMENTARIO = models.CharField(max_length=100)
    TIPO = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.DESCRIPCION + '-' + self.TIPO
