# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prediction',
            old_name='viewpoit',
            new_name='viewpoint',
        ),
    ]
