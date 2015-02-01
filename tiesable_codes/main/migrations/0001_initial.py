# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basic_base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_id', models.IntegerField(null=True)),
                ('person_id', models.IntegerField(null=True)),
                ('prefix', models.CharField(max_length=255, blank=True)),
                ('first_name', models.CharField(max_length=255, blank=True)),
                ('middle_name', models.CharField(max_length=255, blank=True)),
                ('last_name', models.CharField(max_length=255, blank=True)),
                ('suffix', models.CharField(max_length=255, blank=True)),
                ('nickname', models.CharField(max_length=255, blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, choices=[(1, b'male'), (2, b'female'), (9, b'not applicable')])),
                ('birthday', models.DateField(null=True, blank=True)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('photo', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Profile pic', blank=True)),
                ('marital_status', models.CharField(blank=True, max_length=1, choices=[(1, b'single'), (2, b'married')])),
                ('blood_type', models.CharField(blank=True, max_length=1, choices=[(1, b'A'), (2, b'B'), (3, b'AB'), (4, b'O')])),
                ('importance_score', models.CharField(blank=True, max_length=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('familarity_score', models.CharField(blank=True, max_length=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('core_relation_with_me', models.CharField(max_length=255, blank=True)),
                ('how_many_years', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cities_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='company_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='concentration_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='country_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='degree_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='email_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_address', models.EmailField(max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='email_item_name_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='go_location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fk_basic_base_id', models.ForeignKey(to='main.basic_base')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='has_edu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_year', models.IntegerField(null=True, blank=True)),
                ('fk_basic_base_id', models.ForeignKey(to='main.basic_base')),
                ('fk_concentration_id', models.ForeignKey(to='main.concentration_info')),
                ('fk_degree_id', models.ForeignKey(to='main.degree_info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='has_email_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fk_basic_base_id', models.ForeignKey(to='main.basic_base')),
                ('fk_email_id', models.ForeignKey(to='main.email_info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='has_interest_skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(blank=True, max_length=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('fk_basic_base_id', models.ForeignKey(to='main.basic_base')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='has_note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=4, max_length=1, blank=True, choices=[(1, b'work'), (2, b'school'), (3, b'interest/skill'), (4, b'other')])),
                ('note_date', models.DateField(auto_now_add=True)),
                ('reminder_date', models.DateTimeField(null=True, blank=True)),
                ('fk_basic_base_id', models.ForeignKey(to='main.basic_base')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='has_phone_number_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fk_basic_base_id', models.ForeignKey(to='main.basic_base')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='has_sn_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fk_basic_base_id', models.ForeignKey(to='main.basic_base')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='industry_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='interest_skill_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='language_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='location_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('fk_city_id', models.ForeignKey(to='main.cities_info')),
                ('fk_country_id', models.ForeignKey(to='main.country_info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='location_item_name_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='note_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note_content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='phone_item_name_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='phone_number_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.BigIntegerField(null=True, blank=True)),
                ('fk_item_name_id', models.ForeignKey(to='main.phone_item_name_info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='position_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='school_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sn_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn_username', models.CharField(unique=True, max_length=255)),
                ('sn_url', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sn_item_name_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='states_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('fk_country_id', models.ForeignKey(to='main.country_info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='we_meet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('how_or_who', models.CharField(max_length=255, blank=True)),
                ('note', models.TextField(blank=True)),
                ('when', models.DateField(blank=True)),
                ('fk_basic_base_id', models.ForeignKey(to='main.basic_base')),
                ('fk_location_id', models.ForeignKey(to='main.location_info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='work_for',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('fk_basic_base_id', models.ForeignKey(to='main.basic_base')),
                ('fk_company_id', models.ForeignKey(to='main.company_info')),
                ('fk_location_id', models.ForeignKey(to='main.location_info')),
                ('fk_position_id', models.ForeignKey(to='main.position_info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sn_info',
            name='fk_item_name_id',
            field=models.ForeignKey(to='main.sn_item_name_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location_info',
            name='fk_state_id',
            field=models.ForeignKey(to='main.states_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='has_sn_info',
            name='fk_sn_id',
            field=models.ForeignKey(to='main.sn_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='has_phone_number_info',
            name='fk_phone_number_id',
            field=models.ForeignKey(to='main.phone_number_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='has_note',
            name='fk_note_id',
            field=models.ForeignKey(to='main.note_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='has_interest_skill',
            name='fk_interest_skill_id',
            field=models.ForeignKey(to='main.interest_skill_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='has_edu',
            name='fk_location_id',
            field=models.ForeignKey(to='main.location_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='has_edu',
            name='fk_school_id',
            field=models.ForeignKey(to='main.school_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='go_location',
            name='fk_location_id',
            field=models.ForeignKey(to='main.location_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='go_location',
            name='fk_location_item_name_id',
            field=models.ForeignKey(to='main.location_item_name_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='email_info',
            name='fk_item_name_id',
            field=models.ForeignKey(to='main.email_item_name_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company_info',
            name='fk_industry_id',
            field=models.ForeignKey(to='main.industry_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cities_info',
            name='fk_state_id',
            field=models.ForeignKey(to='main.states_info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basic_base',
            name='fk_languages',
            field=models.ManyToManyField(to='main.language_info'),
            preserve_default=True,
        ),
    ]
