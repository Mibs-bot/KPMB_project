# Generated by Django 5.0.7 on 2024-09-18 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpp', '0006_remove_student_studentcode_delete_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentor',
            fields=[
                ('mentorcode', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('mentorname', models.TextField(max_length=50)),
                ('mentoraccdate', models.DateField(null=True)),
            ],
        ),
    ]
