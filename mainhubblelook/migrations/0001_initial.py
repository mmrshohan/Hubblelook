# Generated by Django 2.0.6 on 2018-07-23 20:05

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_tumbline', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('product_name', models.CharField(max_length=50)),
                ('launched_time', models.DateField()),
                ('pub_time', models.DateTimeField(auto_now=True, verbose_name='Publish time')),
                ('causel', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_url', models.URLField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('Prices', models.IntegerField(blank=True, null=True)),
                ('details', ckeditor.fields.RichTextField(default=None)),
            ],
            options={
                'verbose_name': 'Product',
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Initial_keyword_choices', models.CharField(blank=True, choices=[('General', 'GENERAL'), ('Product', 'PRODUCT'), ('Economics', 'ECONOMICS'), ('Market', 'MARKET'), ('Financial market', 'FINANCIAL MARKET')], default='General', max_length=10, null=True)),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('article_pub_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Micro Article',
                'ordering': ['-article_pub_time'],
            },
        ),
        migrations.CreateModel(
            name='QuickWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=2000, null=True)),
                ('pub_time', models.DateTimeField(auto_now=True, verbose_name='Publish time')),
                ('description', models.CharField(max_length=150)),
                ('Initial_keyword_choices', models.CharField(blank=True, choices=[('I think', 'I THINK'), ('Prototype', 'FEEDBACK'), ('Feedback', 'GOOD PART'), ('Good part', 'BAD PART'), ('Bad part', 'PROTOTYPE'), ('Review', 'REVIEW'), ('Ask', 'ASK'), ('Financial market', 'FINANCIAL MARKET')], default='I think', max_length=100, null=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Micro Thought',
                'ordering': ['-pub_time'],
            },
        ),
        migrations.CreateModel(
            name='UserContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('topic', models.CharField(help_text='Do not write more than 200 words', max_length=200)),
                ('write', models.TextField()),
            ],
        ),
    ]
