# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('notes', models.TextField(verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'building',
                'verbose_name_plural': 'buildings',
            },
        ),
        migrations.CreateModel(
            name='BuildingFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('file', models.FileField(upload_to=b'building', verbose_name='file')),
                ('building', models.ForeignKey(verbose_name='building', to='MainSystem.Building')),
            ],
            options={
                'verbose_name': 'file',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('date', models.DateField(verbose_name='date')),
                ('amount', models.DecimalField(default=0, verbose_name='amount', max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'one-time discount',
                'verbose_name_plural': 'one-time discount',
            },
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('date', models.DateField(verbose_name='date')),
                ('amount', models.DecimalField(default=0, verbose_name='amount', max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'one-time fee',
                'verbose_name_plural': 'one-time fees',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1024, verbose_name='description')),
                ('date', models.DateField(verbose_name='date')),
                ('amount', models.DecimalField(verbose_name='amount', max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'payment received from tenant',
                'verbose_name_plural': 'payments received from tenant',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('address', models.TextField(verbose_name='address')),
                ('notes', models.TextField(verbose_name='notes', blank=True)),
                ('area', models.DecimalField(verbose_name='surface area', max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('rooms', models.DecimalField(verbose_name='number of rooms', max_digits=2, decimal_places=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='building', blank=True, to='MainSystem.Building', null=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'property',
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
            name='PropertyFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('file', models.FileField(upload_to=b'property', verbose_name='file')),
                ('property', models.ForeignKey(verbose_name='property', to='MainSystem.Property')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1024, verbose_name='description')),
                ('date', models.DateField(verbose_name='date')),
                ('amount', models.DecimalField(verbose_name='amount', max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'money transfer to tenant',
                'verbose_name_plural': 'money transfers to tenant',
            },
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='date')),
                ('text', models.TextField(verbose_name='description')),
                ('read', models.BooleanField(default=False, verbose_name='mark as read')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'reminder',
                'verbose_name_plural': 'reminders',
            },
        ),
        migrations.CreateModel(
            name='RentRevision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(help_text='date at which the rent generation should stop (non-inclusive)', null=True, verbose_name='end date', blank=True)),
                ('rent', models.DecimalField(verbose_name='monthly rent', max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('provision', models.DecimalField(verbose_name='monthly provision', max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ['-start_date'],
                'verbose_name': 'rent revision',
                'verbose_name_plural': 'rent revisions',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('tenancy_begin_date', models.DateField(verbose_name='tenancy begin date')),
                ('tenancy_end_date', models.DateField(null=True, verbose_name='tenancy end date', blank=True)),
                ('deposit', models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], help_text='A sum of money asked to tenant on day 1. It is payed back in full on the final day of the tenancy', verbose_name='deposit')),
                ('contact_info', models.TextField(verbose_name='contact info', blank=True)),
                ('notes', models.TextField(verbose_name='notes', blank=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='property', to='MainSystem.Property')),
            ],
            options={
                'ordering': ['tenancy_end_date', 'name'],
                'verbose_name': 'tenant',
                'verbose_name_plural': 'tenants',
            },
        ),
        migrations.CreateModel(
            name='TenantFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('file', models.FileField(upload_to=b'tenant', verbose_name='file')),
                ('tenant', models.ForeignKey(verbose_name='tenant', to='MainSystem.Tenant')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
        ),
        migrations.AddField(
            model_name='rentrevision',
            name='tenant',
            field=models.ForeignKey(verbose_name='tenant', to='MainSystem.Tenant'),
        ),
        migrations.AddField(
            model_name='reminder',
            name='tenant',
            field=models.ForeignKey(verbose_name='tenant', to='MainSystem.Tenant'),
        ),
        migrations.AddField(
            model_name='refund',
            name='tenant',
            field=models.ForeignKey(verbose_name='tenant', to='MainSystem.Tenant'),
        ),
        migrations.AddField(
            model_name='payment',
            name='tenant',
            field=models.ForeignKey(verbose_name='tenant', to='MainSystem.Tenant'),
        ),
        migrations.AddField(
            model_name='fee',
            name='tenant',
            field=models.ForeignKey(verbose_name='tenant', to='MainSystem.Tenant'),
        ),
        migrations.AddField(
            model_name='discount',
            name='tenant',
            field=models.ForeignKey(verbose_name='tenant', to='MainSystem.Tenant'),
        ),
        migrations.CreateModel(
            name='TenantReminders',
            fields=[
            ],
            options={
                'verbose_name': 'tenant reminder list',
                'proxy': True,
                'verbose_name_plural': 'tenants reminder lists',
            },
            bases=('MainSystem.tenant',),
        ),
    ]
