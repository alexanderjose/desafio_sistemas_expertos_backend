# Generated by Django 3.2.8 on 2021-10-24 04:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('estado', models.IntegerField(choices=[(1, 'Abierto'), (2, 'Pendiente'), (3, 'En Proceso'), (4, 'Resuelto'), (5, 'Cerrado')])),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]