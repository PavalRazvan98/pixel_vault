# Generated by Django 5.1 on 2024-09-10 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_systemrequirement_graphics'),
        ('misc', '0009_add_unique'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Badges',
            new_name='Badge',
        ),
    ]
