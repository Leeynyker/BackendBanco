from .models import product
from rest_framework import serializers


class productSerializer(serializers.ModelSerializer):
  class Meta:
      model = product
      fields = (
          "productoId",
          "productoNombre",
          "productoTipo",
          "productoTitular",
          "productoSaldo",
          "productoCuota",
      )