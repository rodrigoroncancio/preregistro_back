# Generated by Django 5.0.4 on 2025-02-22 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_acquisitionfarm_civilstatus_condition_department_education_familyrelationships_healthaffiliationtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='roles',
            field=models.TextField(blank=True, null=True),
        ),
    ]
