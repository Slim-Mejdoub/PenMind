# Generated by Django 4.2.1 on 2023-08-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyMood', '0003_datamood_user_alter_datamood_mood_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamood',
            name='mood_score',
            field=models.CharField(max_length=1),
        ),
    ]
