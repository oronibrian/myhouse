# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSystem', '0011_auto_20161206_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='username',
        ),
    ]
