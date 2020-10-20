from django.db import models

# Create your models here.

class Producto(models.Model):
    tipo = models.CharField(max_length=60, primary_key=True)
    marca = models.CharField(max_length=60)

    def __str__(self):
        return self.tipo


class Insumo(models.Model):
    nombre = models.CharField(max_length=120, primary_key=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.TextField()
    imagen=models.ImageField(upload_to='productos',null=True)
    Producto= models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class SliderIndex(models.Model):
    indet = models.CharField(max_length=15,primary_key=True)
    imagen = models.ImageField(upload_to='car', null=True)

    
    def __str__(self):
        return self.indet

class MisionVision (models.Model):
    indet = models.CharField(max_length=15,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.indet



