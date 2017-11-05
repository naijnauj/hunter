# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_auto_20171025_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态', choices=[(0, '正常'), (-1, '删除')]),
            preserve_default=False,
        ),
    ]
