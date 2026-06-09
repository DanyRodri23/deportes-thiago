from django.db import models


class Producto(models.Model):

    CATEGORIAS = [
        ('camisa', 'Camisa'),
        ('pantaloneta', 'Pantaloneta'),
        ('gorra', 'Gorra'),
        ('accesorio', 'Accesorio'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )

    imagen = models.ImageField(
        upload_to='productos/',
        null=True,
        blank=True
    )

    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre