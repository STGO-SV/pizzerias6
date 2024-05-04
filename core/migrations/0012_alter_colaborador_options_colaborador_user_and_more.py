# Generated by Django 5.0.3 on 2024-05-04 14:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_cliente_email_alter_cliente_telefono_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colaborador',
            options={'permissions': [('agregar_pedido', 'Puede agregar pedido'), ('ver_detalles', 'Puede ver detalles'), ('editar_pedido', 'Puede editar pedido'), ('eliminar_pedido', 'Puede eliminar pedido')]},
        ),
        migrations.AddField(
            model_name='colaborador',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colaborador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='cargo',
            field=models.CharField(choices=[('Driver', 'Driver'), ('Operario', 'Operario'), ('Jefe de turno', 'Jefe de turno'), ('Gerente', 'Gerente')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='medio_pago',
            field=models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('mercadopago', 'Mercadopago'), ('sodexo', 'Sodexo')], max_length=100, verbose_name='Medio de pago'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tipo_entrega',
            field=models.CharField(choices=[('delivery', 'Delivery'), ('retiro', 'Retiro en tienda'), ('consumo', 'Consumo en local')], max_length=50, verbose_name='Tipo entrega'),
        ),
    ]
