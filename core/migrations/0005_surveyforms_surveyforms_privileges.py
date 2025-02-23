# Generated by Django 5.0.4 on 2025-02-22 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_staff_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyForms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('survey', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyForms_Privileges',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.IntegerField(blank=True, null=True)),
                ('privilege', models.TextField(blank=True, null=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.surveyforms')),
            ],
        ),
    ]
