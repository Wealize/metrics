# Generated by Django 3.1.7 on 2021-02-22 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0007_auto_20210222_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprintmember',
            name='dedication_percentage',
        ),
    ]
