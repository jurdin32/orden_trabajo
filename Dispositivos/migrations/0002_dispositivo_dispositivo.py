# Generated by Django 3.2.6 on 2021-08-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dispositivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='dispositivo',
            field=models.BooleanField(default=True),
        ),
    ]