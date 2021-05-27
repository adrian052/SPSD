# Generated by Django 3.2 on 2021-05-27 18:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('presupuestos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=256, verbose_name='Descripción')),
                ('proveedor', models.CharField(max_length=200, verbose_name='Proveedor')),
                ('precio_unitario', models.FloatField(max_length=9, verbose_name='Precio Unitario')),
                ('cantidad', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)], verbose_name='Cantidad')),
                ('precio_total', models.FloatField(editable=False, validators=[django.core.validators.MaxValueValidator(1000000), django.core.validators.MinValueValidator(0)], verbose_name='Total')),
                ('fecha', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('factura', models.FileField(blank=True, max_length=254, null=True, upload_to='facturas', verbose_name='Factura')),
                ('id_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuestos.actividad')),
            ],
        ),
    ]
