# Generated by Django 4.1.3 on 2022-12-27 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='hashtag',
        ),
    ]