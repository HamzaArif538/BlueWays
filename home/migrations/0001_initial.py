# Generated by Django 4.2.6 on 2023-11-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=200, null=True)),
                ('car_model', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='car_pictures/')),
            ],
        ),
    ]
