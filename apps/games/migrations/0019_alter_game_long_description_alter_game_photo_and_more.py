# Generated by Django 5.1 on 2024-09-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0018_rename_storage_systemrequirement_storage_mb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='long_description',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='photo',
            field=models.URLField(blank=True, default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='video',
            field=models.URLField(blank=True, default=1, max_length=1000),
            preserve_default=False,
        ),
    ]