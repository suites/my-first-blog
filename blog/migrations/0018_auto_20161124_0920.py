# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20161124_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberofmeeting',
            name='meeting_number',
            field=models.ForeignKey(related_name='member_meeting', to='blog.NumberOfMeeting'),
        ),
    ]
