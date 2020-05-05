# Generated by Django 3.0.6 on 2020-05-05 08:40

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('started_at', models.DateTimeField()),
                ('number_weeks', models.IntegerField(default=1)),
                ('finished_at', models.DateTimeField()),
                ('total_stories', models.IntegerField(blank=True, default=0, null=True)),
                ('stories_done', models.IntegerField(blank=True, default=0, null=True)),
                ('total_bugs', models.IntegerField(blank=True, default=0, null=True)),
                ('bugs_done', models.IntegerField(blank=True, default=0, null=True)),
                ('half_sprint_issues', models.IntegerField(blank=True, default=0, null=True)),
                ('last_release', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]