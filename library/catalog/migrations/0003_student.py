# Generated by Django 2.0 on 2017-12-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(max_length=10)),
                ('student_name', models.CharField(max_length=100)),
            ],
        ),
    ]
