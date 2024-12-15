# Generated by Django 5.1.4 on 2024-12-15 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Project', max_length=32)),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
    ]
