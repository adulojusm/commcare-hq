# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 19:09
from __future__ import unicode_literals
from __future__ import absolute_import

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0030_softwareplan_max_domains'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaccount',
            name='billing_admin_emails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254),
                                                            default=list, size=None, blank=True),
        ),
    ]
