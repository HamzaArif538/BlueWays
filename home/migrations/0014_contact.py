# Generated by Django 4.2.6 on 2023-12-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_booking_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=13, null=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]
