# Generated by Django 4.1.3 on 2022-12-28 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_remove_project_hashtag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='check_like',
            new_name='is_like',
        ),
    ]