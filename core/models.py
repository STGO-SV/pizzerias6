from django.db import models

# Create your models here.

class Colaborador(models.Model):
    rut = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.nombres} - {self.cargo}"