# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companyname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=120)),
                ('admincontact', models.IntegerField()),
                ('staffcontact', models.IntegerField()),
                ('ownercontact', models.IntegerField()),
                ('emailaddress', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='tenant',
            name='user',
            field=models.ForeignKey(default=b'admin', to=settings.AUTH_USER_MODEL),
        ),
    ]
