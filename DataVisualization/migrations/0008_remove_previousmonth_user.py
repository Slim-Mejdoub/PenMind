# Generated by Django 4.2.1 on 2023-08-10 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataVisualization', '0007_alter_previousmonth_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='previousmonth',
            name='user',
        ),
    ]
