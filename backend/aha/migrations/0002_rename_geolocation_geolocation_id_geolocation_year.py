# Generated by Django 4.2.6 on 2023-10-30 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aha', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geolocation',
            old_name='geolocation',
            new_name='id',
        ),
        migrations.AddField(
            model_name='geolocation',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
