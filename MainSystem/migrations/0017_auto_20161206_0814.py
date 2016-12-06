# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSystem', '0016_auto_20161206_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='username',
            field=models.CharField(default=1, max_length=255, verbose_name='username'),
        ),
    ]
