# Generated by Django 4.2.1 on 2023-08-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyMood', '0008_alter_datamood_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamood',
            name='mood_date',
            field=models.DateTimeField(),
        ),
    ]
