# Generated by Django 3.0.3 on 2020-06-03 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20200530_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheltuieli',
            name='categorie',
            field=models.CharField(choices=[('cumparaturi', 'Cumparaturi'), ('masina', 'Masina'), ('casa', 'Casa'), ('timpLiber', 'Timp Liber'), ('diverse', 'Diverse')], default='diverse', max_length=15),
        ),
        migrations.DeleteModel(
            name='Sold',
        ),
    ]
