# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlatText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('text_type', models.CharField(default=b'html', max_length=128, choices=[(b'html', 'HTML'), (b'plain', 'Plain text'), (b'markdown', 'Markdown'), (b'django', 'Django template')])),
                ('text', models.TextField(blank=True)),
                ('processed_text', models.TextField(editable=False, blank=True)),
                ('note', models.CharField(max_length=200, blank=True)),
                ('related_url', models.CharField(max_length=400, blank=True)),
            ],
            options={
                'verbose_name': 'flattext',
                'verbose_name_plural': 'flattexts',
            },
        ),
    ]
