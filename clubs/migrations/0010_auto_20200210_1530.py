# Generated by Django 3.0.2 on 2020-02-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0009_auto_20200210_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='type',
            field=models.CharField(choices=[('Hard', 'Hard'), ('Grass', 'Grass'), ('Clay', 'Clay'), ('Carpet', 'Carpet')], max_length=100),
        ),
    ]
