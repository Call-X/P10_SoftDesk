# Generated by Django 4.0.3 on 2022-04-21 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_rename_project_issues_project_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='author_user_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='issue',
            new_name='issue_id',
        ),
    ]