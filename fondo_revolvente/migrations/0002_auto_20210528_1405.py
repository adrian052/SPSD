# Generated by Django 3.1.3 on 2021-05-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondo_revolvente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastorevolvente',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
