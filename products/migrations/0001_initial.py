# Generated by Django 4.0 on 2022-09-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('productoId', models.BigAutoField(primary_key=True, serialize=False)),
                ('productoNombre', models.CharField(max_length=50)),
                ('productoTipo', models.CharField(max_length=20)),
                ('productoTitular', models.CharField(max_length=11)),
                ('productoSaldo', models.FloatField()),
                ('productoCuota', models.FloatField()),
            ],
        ),
    ]