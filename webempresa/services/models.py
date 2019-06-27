from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta: # Agrega metadatos al modelo
        verbose_name = "Servicio" # Para que en el admin se vea Servicio en lugar de project
        verbose_name_plural = "Servicios" # Para que en el admin se vea Servicios en lugar de projects
        ordering = ["-created"] # Ordenar el modelo por 'created' descendente

    def __str__(self):
        return self.title # Asi mostrara el nombre del servicio en ligar de 'Service object (n)'