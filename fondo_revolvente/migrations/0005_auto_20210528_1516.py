# Generated by Django 3.1.3 on 2021-05-28 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondo_revolvente', '0004_auto_20210528_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fondorevolvente',
            name='anio',
            field=models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Año'),
        ),
    ]