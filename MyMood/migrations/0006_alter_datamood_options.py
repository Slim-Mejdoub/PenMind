# Generated by Django 4.2.1 on 2023-08-04 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMood', '0005_alter_datamood_mood_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datamood',
            options={'ordering': ['id']},
        ),
    ]