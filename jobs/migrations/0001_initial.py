# Generated by Django 2.0.1 on 2018-02-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplyView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_job', models.CharField(max_length=100)),
                ('apply_job', models.EmailField(max_length=100)),
                ('job_location', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=500)),
                ('job_details', models.CharField(max_length=1000)),
            ],
        ),
    ]