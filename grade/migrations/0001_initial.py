# Generated by Django 2.2.4 on 2019-09-02 20:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_score', models.IntegerField(blank=True, null=True)),
                ('final_score', models.IntegerField(blank=True, null=True)),
                ('attendance_score', models.IntegerField(blank=True, null=True)),
                ('total_web_work_score', models.IntegerField(blank=True, null=True)),
                ('total_pre_class_score', models.IntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('datestamp', models.DateField(default=datetime.date.today)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
        ),
    ]
