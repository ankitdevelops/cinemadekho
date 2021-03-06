# Generated by Django 3.2.4 on 2021-06-15 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=300, unique=True)),
                ('movie_name_slug', models.SlugField()),
                ('movie_poster_link', models.URLField(max_length=500)),
                ('movie_on_platform', models.CharField(max_length=100)),
                ('movie_on_platform_link', models.URLField(max_length=2000)),
                ('trailer_youtube_id', models.CharField(max_length=100)),
                ('on_homepage', models.BooleanField(default=False)),
                ('movie_released_date', models.DateField(default=None)),
                ('movie_added_on', models.DateField(auto_now_add=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genre.genre')),
            ],
        ),
    ]
