# Generated by Django 4.2.1 on 2023-08-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DataVisualization', '0002_delete_mooddata_delete_workdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average', models.PositiveIntegerField()),
                ('date', models.CharField(max_length=10)),
            ],
        ),
    ]
