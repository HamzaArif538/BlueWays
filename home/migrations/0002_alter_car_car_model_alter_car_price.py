# Generated by Django 4.2.6 on 2023-11-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
