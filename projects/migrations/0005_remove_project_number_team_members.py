# Generated by Django 3.1.7 on 2021-02-22 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_number_team_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='number_team_members',
        ),
    ]