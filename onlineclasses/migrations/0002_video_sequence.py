# Generated by Django 2.2.8 on 2020-02-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclasses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='sequence',
            field=models.IntegerField(default=1),
        ),
    ]
