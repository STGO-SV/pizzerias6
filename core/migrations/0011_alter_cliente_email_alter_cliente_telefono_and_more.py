# Generated by Django 5.0.3 on 2024-04-15 21:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_pedido_tipo_entrega_alter_pedido_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Ingrese una dirección de correo válida.')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un número válido.', 'required': 'Este campo es obligatorio.'}, validators=[django.core.validators.MaxValueValidator(999999999, message='Ingrese un número de hasta 9 dígitos sin letras o símbolos.'), django.core.validators.MinValueValidator(100000000, message='Ingrese un número de hasta 9 dígitos sin letras o símbolos.')]),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
