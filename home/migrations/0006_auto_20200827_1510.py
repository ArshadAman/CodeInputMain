# Generated by Django 3.1 on 2020-08-27 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200827_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='SocialMedia',
            new_name='socialmedia',
        ),
    ]