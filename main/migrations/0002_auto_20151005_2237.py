# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='cereal',
            name='calories',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='fat',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='protein',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='sodium',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(to='main.Manufacturer'),
        ),
    ]
