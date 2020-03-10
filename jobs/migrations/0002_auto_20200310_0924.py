# Generated by Django 2.2.2 on 2020-03-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='education',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='jobs',
            name='experience',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='jobs',
            name='job_description',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='job_level',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='jobs',
            name='skills',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='jobs',
            name='vacancy_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
