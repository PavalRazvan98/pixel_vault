# Generated by Django 5.1 on 2024-09-11 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0017_rename_memorys_systemrequirement_memory_mb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemrequirement',
            old_name='storage',
            new_name='storage_mb',
        ),
    ]