# Generated by Django 2.2.8 on 2020-02-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclasses', '0007_discussionlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionlink',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
