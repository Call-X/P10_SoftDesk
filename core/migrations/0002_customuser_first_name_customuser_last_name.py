# Generated by Django 4.0.3 on 2022-03-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
