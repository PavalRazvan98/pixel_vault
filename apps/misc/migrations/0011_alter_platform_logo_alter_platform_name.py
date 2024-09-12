# Generated by Django 5.1 on 2024-09-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0010_rename_badges_to_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='logo',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]