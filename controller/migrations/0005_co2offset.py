# Generated by Django 4.2 on 2024-11-01 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0004_powerips'),
    ]

    operations = [
        migrations.CreateModel(
            name='Co2Offset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offset', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]