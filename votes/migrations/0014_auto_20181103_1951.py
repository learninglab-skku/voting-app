# Generated by Django 2.0.2 on 2018-11-03 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0013_auto_20181005_2041'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='response',
            unique_together=set(),
        ),
    ]
