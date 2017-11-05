# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='manager_name',
            new_name='manager',
        ),
    ]
