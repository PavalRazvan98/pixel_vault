# Generated by Django 5.0.7 on 2024-08-28 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_rename_system_requirements_systemrequirements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SystemRequirements',
            new_name='SystemRequirement',
        ),
    ]