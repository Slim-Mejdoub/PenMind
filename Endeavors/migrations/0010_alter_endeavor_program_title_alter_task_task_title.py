# Generated by Django 4.2.1 on 2023-07-13 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Endeavors', '0009_alter_task_endeavor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endeavor',
            name='program_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_title',
            field=models.CharField(max_length=200),
        ),
    ]
