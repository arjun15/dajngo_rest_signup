# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=255, null=True, upload_to='Images/')),
            ],
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]
