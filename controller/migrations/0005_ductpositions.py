# Generated by Django 4.2 on 2024-02-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0004_modeelements_mode_command_alter_mode_mode_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuctPositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
            ],
        ),
    ]