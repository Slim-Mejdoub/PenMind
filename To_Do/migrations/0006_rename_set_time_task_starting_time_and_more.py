# Generated by Django 4.2.1 on 2023-08-05 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_Do', '0005_rename_is_done_task_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='set_time',
            new_name='starting_time',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]