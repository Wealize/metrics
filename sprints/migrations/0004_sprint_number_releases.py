# Generated by Django 3.0.5 on 2020-05-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0003_sprint_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='number_releases',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
