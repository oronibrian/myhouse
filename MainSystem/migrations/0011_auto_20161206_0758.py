# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSystem', '0010_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='user',
        ),
        migrations.AddField(
            model_name='tenant',
            name='username',
            field=models.CharField(default=2, max_length=255, verbose_name='username'),
            preserve_default=False,
        ),
    ]
