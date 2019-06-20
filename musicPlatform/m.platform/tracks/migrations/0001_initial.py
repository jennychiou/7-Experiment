# Generated by Django 2.1 on 2019-06-18 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=30)),
                ('preview_url', models.URLField()),
                ('img_url', models.URLField()),
                ('tracks_number', models.IntegerField()),
                ('release_date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('genres', models.TextField()),
                ('img_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('artist_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('tempo', models.FloatField()),
                ('valence', models.FloatField()),
                ('liveness', models.FloatField()),
                ('instrumentalness', models.FloatField()),
                ('acousticness', models.FloatField()),
                ('speechiness', models.FloatField()),
                ('mode', models.IntegerField()),
                ('loudness', models.FloatField()),
                ('energy', models.FloatField()),
                ('danceability', models.FloatField()),
                ('track_path', models.FilePathField(blank=True)),
                ('sentiment', models.CharField(blank=True, max_length=30)),
                ('preview_url', models.URLField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracks.Album')),
            ],
        ),
        migrations.CreateModel(
            name='RecSysResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('album_img_url', models.URLField()),
                ('track_id', models.CharField(max_length=30)),
                ('recom_method', models.CharField(max_length=2)),
                ('recom_rank', models.IntegerField()),
                ('score', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey20Tracks',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('artist_name', models.CharField(max_length=100)),
                ('artist_id', models.CharField(max_length=30)),
                ('preview_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('results', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UsersLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('track', models.CharField(max_length=30)),
                ('album', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserSurveyCompleted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('complete_date', models.DateTimeField()),
            ],
        ),
    ]
