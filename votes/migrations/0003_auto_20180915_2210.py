# Generated by Django 2.0.2 on 2018-09-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_auto_20180914_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voteresponse',
            name='response',
        ),
        migrations.AddField(
            model_name='voteresponse',
            name='a_response',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='voteresponse',
            name='answer1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='voteresponse',
            name='answer2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='voteresponse',
            name='v_response',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
    ]
