# Generated by Django 3.1.3 on 2021-05-28 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0001_initial'),
        ('fondo_revolvente', '0003_auto_20210528_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fondorevolvente',
            name='anio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='presupuestos.presupuesto', verbose_name='Año'),
        ),
    ]
