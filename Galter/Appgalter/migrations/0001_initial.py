# Generated by Django 4.1.7 on 2023-06-06 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.TextField(max_length=50)),
                ('telefono_cliente', models.TextField(verbose_name=15)),
                ('representante_cliente', models.TextField(max_length=50)),
                ('direccion', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='material',
            fields=[
                ('codi_mate', models.TextField(max_length=10, primary_key=True, serialize=False)),
                ('nomb_mate', models.TextField(max_length=50)),
                ('proveedor', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('codi_prod', models.TextField(max_length=10, primary_key=True, serialize=False)),
                ('nomb_prod', models.TextField(max_length=100)),
                ('material_prod', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('nombre_proveedor', models.TextField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('codi_usuario', models.TextField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_usuario', models.TextField(max_length=50)),
                ('correo_usuario', models.EmailField(max_length=50)),
                ('pass_ususario', models.TextField(max_length=100)),
                ('tipo_usuario', models.TextField(max_length=30)),
            ],
        ),
    ]