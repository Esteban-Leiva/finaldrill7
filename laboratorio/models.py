from django.db import models

# Create your models here.

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)

class DirectorGeneral(models.Model):
    nombre =  models.CharField(max_length=100)
    laboratorio = models.OneToOneField('Laboratorio', models.DO_NOTHING, db_column='laboratorio', blank=True, null=True)

class Producto (models.Model):
    nombre =  models.CharField(max_length=100)
    laboratorio = models.ForeignKey('Laboratorio', models.DO_NOTHING, db_column='laboratorio', blank=True, null=True)
    f_fabricacion = models.DateTimeField(blank=True, null=True)
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)