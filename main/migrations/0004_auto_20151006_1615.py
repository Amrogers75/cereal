# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151006_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='cereal',
            name='carbs',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='cups_per_serving',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='dietary_fiber',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='display_shelf',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='potassium',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='serving_size_weight',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='vitamins_and_minerals',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
