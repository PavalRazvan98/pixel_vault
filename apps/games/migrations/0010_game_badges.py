# Generated by Django 5.0.7 on 2024-08-28 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_game_features'),
        ('misc', '0007_badges'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='badges',
            field=models.ManyToManyField(to='misc.badges'),
        ),
    ]
