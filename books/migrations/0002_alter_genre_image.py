# Generated by Django 5.0.6 on 2025-01-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.CharField(max_length=2500),
        ),
    ]
