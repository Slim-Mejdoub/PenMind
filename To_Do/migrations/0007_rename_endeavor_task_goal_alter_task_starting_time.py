# Generated by Django 4.2.1 on 2023-08-05 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_Do', '0006_rename_set_time_task_starting_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='endeavor',
            new_name='goal',
        ),
        migrations.AlterField(
            model_name='task',
            name='starting_time',
            field=models.DateTimeField(),
        ),
    ]
