# Generated by Django 2.0 on 2018-01-06 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180106_0933'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]