# Generated by Django 5.0.7 on 2024-08-16 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpp', '0003_programme_programmeduration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programme',
            old_name='Programmeduration',
            new_name='programmeduration',
        ),
    ]
