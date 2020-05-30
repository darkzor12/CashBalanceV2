# Generated by Django 3.0.3 on 2020-05-08 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venituri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sumaVenit', models.FloatField()),
                ('descriere', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('note', models.CharField(max_length=80)),
                ('atasament_cheltuieli', models.ImageField(blank=True, upload_to='atasament_venituri')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baniCheltuiti', models.FloatField(blank=True)),
                ('baniVenituri', models.FloatField(blank=True)),
                ('sold', models.FloatField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cheltuieli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sumaCheltuita', models.FloatField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('note', models.CharField(max_length=80)),
                ('atasament_cheltuieli', models.ImageField(blank=True, upload_to='atasament_cheltuieli')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
