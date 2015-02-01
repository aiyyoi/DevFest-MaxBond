# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_base',
            name='blood_type',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', b'A'), (b'2', b'B'), (b'3', b'AB'), (b'4', b'O')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basic_base',
            name='familarity_score',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basic_base',
            name='gender',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', b'male'), (b'2', b'female'), (b'9', b'not applicable')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basic_base',
            name='importance_score',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basic_base',
            name='marital_status',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', b'single'), (b'2', b'married')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='has_interest_skill',
            name='level',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='has_note',
            name='category',
            field=models.CharField(default=b'4', max_length=1, blank=True, choices=[(b'1', b'work'), (b'2', b'school'), (b'3', b'interest/skill'), (b'4', b'other')]),
            preserve_default=True,
        ),
    ]
