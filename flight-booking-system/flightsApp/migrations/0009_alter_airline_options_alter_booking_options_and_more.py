# Generated by Django 4.2.1 on 2023-05-25 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightsApp', '0008_remove_flight_flight_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airline',
            options={'ordering': ['Airline_id']},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['booking_id']},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['city_id']},
        ),
        migrations.AlterModelOptions(
            name='flight',
            options={'ordering': ['filght_id']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['user_id']},
        ),
    ]
