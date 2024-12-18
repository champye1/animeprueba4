from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='equipos/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class JugadorProfesional(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ciudad_nacimiento = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
