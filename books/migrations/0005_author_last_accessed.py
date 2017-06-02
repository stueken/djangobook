# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20170530_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_accessed',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 2, 18, 22, 51, 553608, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
