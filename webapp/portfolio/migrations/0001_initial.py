# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('github', models.CharField(max_length=200)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateField(verbose_name='date started')),
                ('end_date', models.DateField(verbose_name='date ended')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Schooling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateField(verbose_name='date started')),
                ('end_date', models.DateField(verbose_name='date ended')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.FloatField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Applicant')),
            ],
        ),
        migrations.AddField(
            model_name='accomplishment',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Job'),
        ),
    ]