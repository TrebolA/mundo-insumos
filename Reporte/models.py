from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    fecha_de_nacimiento = models.DateField()
    SELECCION = 'SC'
    INDUSTRIAS = (
            (SELECCION, 'Seleccione un tipo industria'),
        )
    industri = models.CharField(
            max_length=3,
            choices=INDUSTRIAS,
            default=SELECCION,
        )
    correo = models.CharField(max_length=100)
    pais
    ciudad