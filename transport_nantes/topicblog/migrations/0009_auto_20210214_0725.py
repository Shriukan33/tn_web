# Generated by Django 3.0.7 on 2021-02-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicblog', '0008_auto_20210104_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicblogpage',
            name='og_image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='topicblogpage',
            name='twitter_image',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]