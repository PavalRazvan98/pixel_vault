# Generated by Django 5.1 on 2024-09-10 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_systemrequirement_graphics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='developer',
            new_name='developers',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='platform',
            new_name='platforms',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='publisher',
            new_name='publishers',
        ),
    ]
