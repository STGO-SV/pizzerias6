# Generated by Django 5.0.3 on 2024-04-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('nombres', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
    ]