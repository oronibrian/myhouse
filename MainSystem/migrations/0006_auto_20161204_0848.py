# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSystem', '0005_auto_20161204_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydetail',
            old_name='contact',
            new_name='admincontact',
        ),
        migrations.AddField(
            model_name='companydetail',
            name='ownercontact',
            field=models.IntegerField(default=14755556),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companydetail',
            name='staffcontact',
            field=models.IntegerField(default=15274596),
            preserve_default=False,
        ),
    ]
