# Generated by Django 4.2.6 on 2023-10-20 07:22

import Store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_estates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Store.models.get_file_path)),
                ('description', models.TextField(max_length=650)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '1. Category',
            },
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.DeleteModel(
            name='Estates',
        ),
    ]