# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainSystem', '0008_remove_tenant_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='user',
            field=models.ForeignKey(default=b'admin', to=settings.AUTH_USER_MODEL),
        ),
    ]
