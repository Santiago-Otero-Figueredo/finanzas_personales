# Generated by Django 3.0.8 on 2020-11-12 00:58

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15, verbose_name='Nombre movimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MaxValueValidator(Decimal('100000000000.00')), django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('descripcion', models.CharField(max_length=30, verbose_name='Descripción')),
                ('fecha_inscripcion', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimiento_tipo', to='movimientos.Tipo', verbose_name='Tipo movimiento')),
            ],
        ),
    ]
