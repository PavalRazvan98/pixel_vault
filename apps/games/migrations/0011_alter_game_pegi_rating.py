# Generated by Django 5.0.7 on 2024-08-28 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_game_badges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='pegi_rating',
            field=models.IntegerField(choices=[(3, 'PEGI 3'), (7, 'PEGI 7'), (12, 'PEGI 12'), (16, 'PEGI 16'), (18, 'PEGI 18')], null=True),
        ),
    ]
