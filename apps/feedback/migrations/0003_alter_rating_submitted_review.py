# Generated by Django 5.1 on 2024-09-09 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_rating_submitted_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='submitted_review',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
