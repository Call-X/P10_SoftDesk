# Generated by Django 4.0.3 on 2022-04-21 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_rename_author_comment_author_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_user_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='issue_id',
            new_name='issue',
        ),
    ]