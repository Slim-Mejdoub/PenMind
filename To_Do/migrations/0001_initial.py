# Generated by Django 3.2.20 on 2023-09-08 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Endeavors', '0014_alter_endeavor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('starting_time', models.DateTimeField()),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('endeavor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_tasks', to='Endeavors.endeavor')),
            ],
        ),
    ]
