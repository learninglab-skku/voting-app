# Generated by Django 2.0.7 on 2020-04-01 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('votes', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(blank=True, max_length=255, null=True)),
                ('video_link', models.CharField(blank=True, max_length=255, null=True)),
                ('index', models.IntegerField(default=1)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('lecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Lecture')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.Question')),
            ],
        ),
        migrations.CreateModel(
            name='VideoTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_vote_submit', models.BooleanField(default=False)),
                ('second_vote_submit', models.BooleanField(default=False)),
                ('discussion_submit', models.BooleanField(default=False)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='onlineclasses.Video')),
            ],
        ),
        migrations.AddField(
            model_name='discussionlink',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='onlineclasses.Video'),
        ),
        migrations.AlterUniqueTogether(
            name='videotracker',
            unique_together={('student', 'video')},
        ),
    ]
