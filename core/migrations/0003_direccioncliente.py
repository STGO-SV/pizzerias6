# Generated by Django 5.0.3 on 2024-04-15 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
            options={
                'db_table': 'CORE_DIRECCIONES_CLIENTE',
            },
        ),
    ]
