# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainSystem', '0006_auto_20161204_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='user',
            field=models.ForeignKey(default=9.0, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
    ]
