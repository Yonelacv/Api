# Generated by Django 4.2.4 on 2023-08-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interacciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaccion_id', models.IntegerField()),
                ('placa', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField()),
                ('hora_entrada', models.DateTimeField()),
                ('hora_salida', models.DateTimeField()),
            ],
        ),
    ]
