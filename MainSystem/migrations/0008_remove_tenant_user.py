# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSystem', '0007_tenant_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='user',
        ),
    ]
