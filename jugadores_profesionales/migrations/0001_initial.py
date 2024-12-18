# Generated by Django 5.1.3 on 2024-12-03 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JugadorProfesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('ciudad_nacimiento', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jugadores_profesionales.campeonato')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jugadores_profesionales.equipo')),
            ],
        ),
    ]