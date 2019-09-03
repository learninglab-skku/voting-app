# Generated by Django 2.1.1 on 2019-09-03 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('due_date', models.CharField(max_length=255, null=True)),
                ('optional_readings', models.CharField(blank=True, max_length=255, null=True)),
                ('video_clip_name_1', models.CharField(blank=True, max_length=255, null=True)),
                ('video_clip_link_1', models.CharField(blank=True, max_length=255, null=True)),
                ('video_clip_name_2', models.CharField(blank=True, max_length=255, null=True)),
                ('video_clip_link_2', models.CharField(blank=True, max_length=255, null=True)),
                ('video_clip_name_3', models.CharField(blank=True, max_length=255, null=True)),
                ('video_clip_link_3', models.CharField(blank=True, max_length=255, null=True)),
                ('questions', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('Course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkTraker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(null=True)),
                ('start_time_video_1', models.DateTimeField(null=True)),
                ('start_time_video_2', models.DateTimeField(null=True)),
                ('start_time_video_3', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('Homework', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homework.Homework')),
                ('Student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='homeworktraker',
            unique_together={('Student', 'Homework')},
        ),
        migrations.AlterUniqueTogether(
            name='homework',
            unique_together={('title', 'Course')},
        ),
    ]
