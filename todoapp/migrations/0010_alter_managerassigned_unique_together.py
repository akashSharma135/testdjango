# Generated by Django 3.2.7 on 2021-09-12 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0009_alter_newuser_username'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='managerassigned',
            unique_together={('manager', 'user')},
        ),
    ]
