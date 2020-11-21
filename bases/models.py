from django.db import models

# Create your models here.


class Imagen(models.Model):
    imagen=models.ImageField(upload_to="claves",null=True )
