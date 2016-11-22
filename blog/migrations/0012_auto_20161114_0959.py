# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20161111_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberofmeeting',
            old_name='member_id',
            new_name='member',
        ),
    ]
