# Generated by Django 5.0.7 on 2024-08-28 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0003_developer_entity_alter_platform_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
