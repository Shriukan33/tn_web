# Generated by Django 3.0.7 on 2021-01-04 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topicblog', '0007_auto_20210103_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicblogpage',
            old_name='bullet_text_1',
            new_name='bullet_text_1_md',
        ),
        migrations.RenameField(
            model_name='topicblogpage',
            old_name='bullet_text_2',
            new_name='bullet_text_2_md',
        ),
        migrations.RenameField(
            model_name='topicblogpage',
            old_name='bullet_text_3',
            new_name='bullet_text_3_md',
        ),
        migrations.RenameField(
            model_name='topicblogpage',
            old_name='bullet_text_4',
            new_name='bullet_text_4_md',
        ),
        migrations.RenameField(
            model_name='topicblogpage',
            old_name='bullet_text_5',
            new_name='bullet_text_5_md',
        ),
    ]