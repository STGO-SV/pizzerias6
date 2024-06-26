# Generated by Django 5.0.3 on 2024-04-15 20:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_pedido_fecha_alter_pedido_hora_pedido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='tipo_entrega',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Tipo entrega'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha del pedido'),
        ),
    ]
