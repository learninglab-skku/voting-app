# Generated by Django 2.0.2 on 2018-09-22 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_lecture_title'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Section'),
        ),
    ]
