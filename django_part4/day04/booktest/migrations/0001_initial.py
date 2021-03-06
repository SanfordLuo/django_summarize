# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('pub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('comment', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'tb_book',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('gender', models.BooleanField(default=False)),
                ('content', models.CharField(max_length=200)),
                ('is_delete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo')),
            ],
        ),
    ]
