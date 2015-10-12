# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151006_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='cereal',
            name='sugars',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
