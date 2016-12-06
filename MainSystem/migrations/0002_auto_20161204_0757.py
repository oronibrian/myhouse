# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildingfile',
            name='building',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='fee',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='property',
            name='building',
        ),
        migrations.RemoveField(
            model_name='propertyfile',
            name='property',
        ),
        migrations.RemoveField(
            model_name='refund',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='rentrevision',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='property',
        ),
        migrations.RemoveField(
            model_name='tenantfile',
            name='tenant',
        ),
        migrations.DeleteModel(
            name='TenantReminders',
        ),
        migrations.DeleteModel(
            name='Building',
        ),
        migrations.DeleteModel(
            name='BuildingFile',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='Fee',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='PropertyFile',
        ),
        migrations.DeleteModel(
            name='Refund',
        ),
        migrations.DeleteModel(
            name='Reminder',
        ),
        migrations.DeleteModel(
            name='RentRevision',
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
        migrations.DeleteModel(
            name='TenantFile',
        ),
    ]
