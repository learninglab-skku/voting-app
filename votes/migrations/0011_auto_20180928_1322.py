# Generated by Django 2.0.2 on 2018-09-28 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0010_auto_20180928_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='contents',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
