# Generated by Django 4.0.4 on 2022-06-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0007_book_dostepna'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='dostepna',
            new_name='dostepne',
        ),
        migrations.AddField(
            model_name='cd',
            name='dostepne',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='dostepne',
            field=models.BooleanField(default=True),
        ),
    ]