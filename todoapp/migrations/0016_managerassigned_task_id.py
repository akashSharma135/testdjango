# Generated by Django 3.2.7 on 2021-09-13 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_remove_task_manager_assigned'),
        ('todoapp', '0015_remove_managerassigned_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerassigned',
            name='task_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task', to='taskapp.task'),
        ),
    ]
