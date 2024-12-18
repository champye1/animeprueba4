from django.db import models

# Create your models here.

class Galeria(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    author=models.CharField(max_length=200)
    fecha_estreno = models.DateField(verbose_name='Fecha de estreno', null=True, blank=True)
    imagen=models.ImageField(upload_to='galeria', null=True, blank=True)


    class Meta:
        verbose_name='Galeria'
        verbose_name_plural='Galerias'

    def __str__(self):
        return str(self.title)

