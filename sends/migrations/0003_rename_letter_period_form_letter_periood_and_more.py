# Generated by Django 4.1.5 on 2023-01-24 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sends', '0002_collection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='letter_period',
            new_name='letter_periood',
        ),
        migrations.RenameField(
            model_name='newsletter',
            old_name='letter_period',
            new_name='letter_periood',
        ),
    ]
