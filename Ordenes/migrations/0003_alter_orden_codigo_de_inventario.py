# Generated by Django 3.2.6 on 2021-08-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordenes', '0002_orden_aprobado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='codigo_de_inventario',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
