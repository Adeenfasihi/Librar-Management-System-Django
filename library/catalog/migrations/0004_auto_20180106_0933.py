# Generated by Django 2.0 on 2018-01-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(max_length=10)),
                ('student_name', models.CharField(max_length=100)),
                ('class_section', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
