# Generated by Django 4.1.2 on 2022-10-29 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_copialivro_emprestado_para_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='copialivro',
            options={'ordering': ['devolucao'], 'permissions': (('pode_marcar_copia_como_devolvida', 'Marca a cópia como devolvida'),)},
        ),
    ]
