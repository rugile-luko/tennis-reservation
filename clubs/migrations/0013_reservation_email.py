# Generated by Django 3.0.2 on 2020-02-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0012_reservation_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
