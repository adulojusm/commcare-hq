# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-27 15:34
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import migrations

from corehq.sql_db.operations import HqRunSQL


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0030_one_synclog_per_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='applicationstatusfact',
            unique_together=set([]),
        ),
        HqRunSQL(
            """
            CREATE UNIQUE INDEX applicationstatusfact_unique_app_user
            ON warehouse_applicationstatusfact (user_dim_id, COALESCE(app_dim_id, -1))
            """
        )
    ]
