# Generated by Django 2.1.2 on 2018-10-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormularioAdopcion', '0002_auto_20181027_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
