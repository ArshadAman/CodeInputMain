# Generated by Django 3.1 on 2021-05-29 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_delete_coursecomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='youtube_id',
            new_name='playlist_id',
        ),
    ]
