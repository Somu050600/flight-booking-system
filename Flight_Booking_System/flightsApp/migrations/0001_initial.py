# Generated by Django 4.2 on 2023-04-29 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='airline',
            fields=[
                ('Airline_id', models.AutoField(primary_key=True, serialize=False)),
                ('Airline_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_code', models.CharField(max_length=5)),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('uset_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField(default=1978)),
                ('passport_number', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='flight',
            fields=[
                ('filght_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=2005)),
                ('number_of_seats', models.IntegerField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('airline_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightsApp.airline')),
                ('arr_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flightsApp.city')),
                ('des_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='flightsApp.city')),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightsApp.flight')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightsApp.user')),
            ],
        ),
    ]
