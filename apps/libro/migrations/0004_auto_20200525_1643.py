# Generated by Django 3.0.6 on 2020-05-25 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Autor'),
        ),
    ]
