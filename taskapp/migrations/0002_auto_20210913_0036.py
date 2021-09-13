# Generated by Django 3.2.7 on 2021-09-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_task',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.IntegerField(choices=[(0, 'Not Completed'), (1, 'Completed')], default=0, verbose_name='task status'),
        ),
    ]
