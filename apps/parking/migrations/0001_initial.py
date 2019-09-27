# Generated by Django 2.2.5 on 2019-09-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_colour', models.CharField(max_length=255)),
                ('car_number', models.CharField(max_length=255)),
                ('is_parked', models.BooleanField(default=False)),
                ('last_entry', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]