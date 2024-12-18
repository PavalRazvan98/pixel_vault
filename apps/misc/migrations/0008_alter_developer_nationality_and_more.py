# Generated by Django 5.0.7 on 2024-08-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0007_badges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='nationality',
            field=models.CharField(choices=[('Usa', 'Usa'), ('France', 'France'), ('Germany', 'Germany'), ('Japan', 'Japan'), ('China', 'China'), ('Uk', 'Uk'), ('Russian', 'Russian'), ('Poland', 'Poland'), ('Canada', 'Canada'), ('Unknown', 'Unknown')], default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='nationality',
            field=models.CharField(choices=[('Usa', 'Usa'), ('France', 'France'), ('Germany', 'Germany'), ('Japan', 'Japan'), ('China', 'China'), ('Uk', 'Uk'), ('Russian', 'Russian'), ('Poland', 'Poland'), ('Canada', 'Canada'), ('Unknown', 'Unknown')], default='Unknown', max_length=50),
        ),
    ]
