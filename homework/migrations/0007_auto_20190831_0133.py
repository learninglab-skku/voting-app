# Generated by Django 2.1.1 on 2019-08-31 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0006_auto_20190831_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='video_clip_name_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='video_clip_name_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='video_clip_name_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]