# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigvs', '0002_auto_20160509_0546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bigvs',
            options={'ordering': ('-words_weight',), 'managed': False, 'verbose_name': '\u5927V', 'verbose_name_plural': '\u5927V'},
        ),
    ]
