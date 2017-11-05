# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20171024_2311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': '板块', 'verbose_name_plural': '板块aaa'},
        ),
    ]
