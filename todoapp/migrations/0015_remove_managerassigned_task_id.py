# Generated by Django 3.2.7 on 2021-09-13 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0014_alter_managerassigned_task_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managerassigned',
            name='task_id',
        ),
    ]
