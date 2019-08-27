# Generated by Django 2.2.4 on 2019-08-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='contents',
        ),
        migrations.AlterField(
            model_name='homework',
            name='video_clip_link_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='video_clip_link_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='video_clip_link_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
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
