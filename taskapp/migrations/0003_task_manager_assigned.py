# Generated by Django 3.2.7 on 2021-09-13 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0015_remove_managerassigned_task_id'),
        ('taskapp', '0002_auto_20210913_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='manager_assigned',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todoapp.managerassigned'),
        ),
    ]
