# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSystem', '0004_companydetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompanyDetails',
            new_name='CompanyDetail',
        ),
    ]