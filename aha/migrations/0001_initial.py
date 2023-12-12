# Generated by Django 4.2.6 on 2023-10-22 02:46

from django.db import migrations, models
import django.db.models.deletion
import pandas as pd

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('geolocation', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('region', models.TextField()),
                ('latitute', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('type', models.TextField()),
                ('title', models.TextField()),
                ('paper', models.TextField()),
                ('topic', models.TextField()),
                ('affiliated_societies', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('institution', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('geolocation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geolocation_id', to='aha.geolocation')),
            ],
        ),
      
    ]