# Generated by Django 2.0.2 on 2018-09-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_auto_20180921_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
                ('survived', models.BooleanField()),
                ('age', models.FloatField()),
                ('ticket_class', models.PositiveSmallIntegerField()),
                ('embarked', models.CharField(max_length=255)),
            ],
        ),
    ]
