from django.db import models

# Create your models here.
class product(models.Model):
  productoId = models.BigAutoField(primary_key=True)
  productoNombre = models.CharField(max_length=50)
  productoTipo = models.CharField(max_length=20)
  productoTitular = models.CharField(max_length=11)
  productoSaldo = models.FloatField()
  productoCuota = models.FloatField()
  
  def __str__(self) -> str:
    return self.productoNombre