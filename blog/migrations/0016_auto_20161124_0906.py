# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_numberofmeeting_deposit_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberofmeeting',
            name='meeting_number',
        ),
        migrations.AddField(
            model_name='numberofmeeting',
            name='meeting_member',
            field=models.ForeignKey(to='blog.MemberOfMeeting', null=True, related_name='member_meeting'),
        ),
    ]
