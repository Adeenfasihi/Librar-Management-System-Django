# Generated by Django 2.0 on 2018-01-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180106_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='return_date',
            field=models.DateTimeField(default='', verbose_name='Date of return'),
        ),
    ]
