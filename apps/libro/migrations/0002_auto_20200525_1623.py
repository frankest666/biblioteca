# Generated by Django 3.0.6 on 2020-05-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción'),
        ),
    ]
