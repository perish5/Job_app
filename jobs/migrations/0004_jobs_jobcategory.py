# Generated by Django 2.2.2 on 2020-02-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_jobcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='jobcategory',
            field=models.ManyToManyField(related_name='job_categories', to='jobs.JobCategory'),
        ),
    ]
