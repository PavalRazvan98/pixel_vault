# Generated by Django 5.0.7 on 2024-08-28 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_rename_systemrequirements_systemrequirement'),
        ('misc', '0004_alter_platform_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='pegi_rating',
            field=models.CharField(choices=[(3, 'PEGI 3'), (7, 'PEGI 7'), (12, 'PEGI 12'), (16, 'PEGI 16'), (18, 'PEGI 18')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ManyToManyField(to='misc.publisher'),
        ),
        migrations.AddField(
            model_name='systemrequirement',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='games.game'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='systemrequirement',
            unique_together={('game', 'type', 'os')},
        ),
    ]
