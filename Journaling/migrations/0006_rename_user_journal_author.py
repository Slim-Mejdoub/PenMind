# Generated by Django 4.2.1 on 2023-07-20 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Journaling', '0005_journal_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='user',
            new_name='author',
        ),
    ]
