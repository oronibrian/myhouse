# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('housetitle', models.CharField(max_length=250)),
                ('roomsvacant', models.IntegerField()),
                ('housedescription', models.TextField()),
            ],
        ),
    ]
