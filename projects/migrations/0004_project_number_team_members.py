# Generated by Django 3.0.5 on 2020-05-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_default_sprint_length_in_weeks'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='number_team_members',
            field=models.IntegerField(default=1),
        ),
    ]
