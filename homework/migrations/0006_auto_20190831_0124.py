# Generated by Django 2.1.1 on 2019-08-31 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0005_auto_20190830_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='video_clip_name_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='video_clip_name_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='video_clip_name_3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
