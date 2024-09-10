# Generated by Django 5.0.7 on 2024-08-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_pegi_rating_game_publisher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='long_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='pegi_rating',
            field=models.IntegerField(choices=[(3, 'PEGI 3'), (7, 'PEGI 7'), (12, 'PEGI 12'), (16, 'PEGI 16'), (18, 'PEGI 18')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='photo',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='video',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]