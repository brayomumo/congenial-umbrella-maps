# Generated by Django 3.0.7 on 2020-06-03 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TweetObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=256)),
                ('polarity', models.FloatField()),
                ('subjectivity', models.FloatField()),
                ('mentions', models.CharField(blank=True, max_length=256)),
                ('hashtag', models.CharField(blank=True, max_length=256)),
                ('location', models.CharField(blank=True, max_length=256)),
                ('route', models.CharField(blank=True, max_length=256, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('conditions', models.CharField(blank=True, max_length=256, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date Created')),
            ],
        ),
    ]
