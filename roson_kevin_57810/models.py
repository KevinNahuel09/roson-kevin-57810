from django.db import models

class Zapatilla(models.Model):
    nombre = models.CharField(max_length=100)
    talle = models.IntegerField()
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'zapatilla'
