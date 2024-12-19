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
    nickname = models.CharField(max_length=50)
    equipo = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    # Añade más campos según necesites

    class Meta:
        verbose_name = "Jugador Profesional"
        verbose_name_plural = "Jugadores Profesionales"

    def __str__(self):
        return f"{self.nickname} - {self.equipo}"
