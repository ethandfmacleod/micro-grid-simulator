# Generated by Django 5.1.4 on 2025-01-04 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowsheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=255)),
                ('irradiance', models.FloatField(blank=True, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('wind_speed', models.FloatField(blank=True, null=True)),
                ('humidity', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
