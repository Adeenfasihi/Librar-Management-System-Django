# Generated by Django 2.0 on 2018-01-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180106_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.CharField(default='a', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]