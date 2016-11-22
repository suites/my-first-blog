# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161111_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberofmeeting',
            old_name='meeting_number_id',
            new_name='meeting_number',
        ),
        migrations.RenameField(
            model_name='numberofmeeting',
            old_name='meeting_id',
            new_name='meeting',
        ),
        migrations.RenameField(
            model_name='numberofmeeting',
            old_name='meeting_number',
            new_name='meeting_count',
        ),
    ]
