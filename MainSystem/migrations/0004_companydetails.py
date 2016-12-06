# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSystem', '0003_auto_20161204_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companyname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=120)),
                ('contact', models.IntegerField()),
                ('emailaddress', models.EmailField(max_length=254)),
            ],
        ),
    ]
