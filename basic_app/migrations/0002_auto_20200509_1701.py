# Generated by Django 3.0.3 on 2020-05-09 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venituri',
            old_name='atasament_cheltuieli',
            new_name='atasament_venituri',
        ),
    ]
