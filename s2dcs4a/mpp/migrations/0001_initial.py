# Generated by Django 5.0.7 on 2024-08-13 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('programmecode', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('programmename', models.TextField(max_length=50)),
                ('programmeaccdate', models.DateField(null=True)),
            ],
        ),
    ]
