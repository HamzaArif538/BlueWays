# Generated by Django 4.2.6 on 2023-12-01 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_car_outcityprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('phoneno', models.CharField(max_length=13, null=True)),
                ('date_from', models.DateField(null=True)),
                ('date_to', models.DateField(null=True)),
                ('message', models.TextField(null=True)),
                ('car_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.car')),
            ],
        ),
    ]
