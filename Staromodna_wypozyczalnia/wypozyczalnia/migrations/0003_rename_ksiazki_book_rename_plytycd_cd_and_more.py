# Generated by Django 4.0.4 on 2022-05-23 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0002_alter_plytycd_lista_utworów'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ksiazki',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='PlytyCD',
            new_name='CD',
        ),
        migrations.RenameModel(
            old_name='Filmy',
            new_name='Movie',
        ),
        migrations.RenameModel(
            old_name='Wypozyczalnia',
            new_name='Rental',
        ),
    ]