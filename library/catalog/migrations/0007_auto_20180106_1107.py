# Generated by Django 2.0 on 2018-01-06 11:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180106_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='return_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of return'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.CharField(choices=[('l', 'On loan'), ('a', 'Available')], default='a', max_length=2),
        ),
        migrations.AlterField(
            model_name='issue',
            name='return_date',
            field=models.DateTimeField(verbose_name='Date of return'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]