# Generated by Django 3.0.8 on 2020-08-17 18:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Shannon Gaels vs ____', max_length=255)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='media/club_images/')),
                ('venue', models.CharField(default='Croghan', max_length=255)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('result', models.CharField(blank=True, max_length=255)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fixtures.Category')),
            ],
        ),
    ]
