# Generated by Django 4.2 on 2023-04-30 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
    ]
