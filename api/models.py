from django.db import models

# Create your models here.
class Interacciones(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False)
    placa = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    hora_entrada = models.DateTimeField()
    hora_salida = models.DateTimeField()

    # def __str__(self):
    #     return f"Registro ID: {self.id}, Placa: {self.placa}"