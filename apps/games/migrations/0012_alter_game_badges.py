# Generated by Django 5.0.7 on 2024-08-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_alter_game_pegi_rating'),
        ('misc', '0008_alter_developer_nationality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='badges',
            field=models.ManyToManyField(blank=True, null=True, to='misc.badges'),
        ),
    ]
