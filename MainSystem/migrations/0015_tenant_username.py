# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSystem', '0014_remove_tenant_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='username',
            field=models.CharField(default=b'tenant', max_length=255, verbose_name='username'),
        ),
    ]
