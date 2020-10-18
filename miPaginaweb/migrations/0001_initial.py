# Generated by Django 3.1.1 on 2020-09-30 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('tipo', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('nombre', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miPaginaweb.producto')),
            ],
        ),
    ]