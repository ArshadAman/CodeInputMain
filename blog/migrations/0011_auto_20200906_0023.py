# Generated by Django 3.1 on 2020-09-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200905_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='suggest',
            field=models.CharField(default='None', max_length=200),
        ),
    ]