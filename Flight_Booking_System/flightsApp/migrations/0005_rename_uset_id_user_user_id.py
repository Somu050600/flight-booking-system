# Generated by Django 4.2 on 2023-04-30 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightsApp', '0004_rename_myuser_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uset_id',
            new_name='user_id',
        ),
    ]