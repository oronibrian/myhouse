# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRequests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emailadsress', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=155)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]
