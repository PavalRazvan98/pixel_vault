# Generated by Django 5.0.7 on 2024-08-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0004_alter_platform_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
