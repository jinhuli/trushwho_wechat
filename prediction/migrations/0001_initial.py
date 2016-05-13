# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigvs', '0002_auto_20160509_0546'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('viewpoit', models.CharField(max_length=16, verbose_name='\u89c2\u70b9', choices=[('rise', '\u770b\u591a'), ('drop', '\u770b\u7a7a'), ('bumpy', '\u770b\u5e73')])),
                ('start_datetime', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_datetime', models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('article', models.ForeignKey(verbose_name='\u6587\u7ae0', to='articles.ArticlePostedResults')),
                ('bigv', models.ForeignKey(verbose_name='\u5927V', to='bigvs.BigVs')),
            ],
            options={
                'verbose_name': '\u591a\u7a7a\u770b\u677f',
                'verbose_name_plural': '\u591a\u7a7a\u770b\u677f',
            },
        ),
    ]
