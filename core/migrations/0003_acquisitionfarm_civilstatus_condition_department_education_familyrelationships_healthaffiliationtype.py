# Generated by Django 3.2.15 on 2025-02-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_create_default_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acquisitionfarm',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'AcquisitionFarm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Civilstatus',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
            ],
            options={
                'db_table': 'CivilStatus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'Condition',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('code', models.CharField(db_column='Code', max_length=10, unique=True)),
                ('active', models.BooleanField(db_column='Active', default=True, null=True)),
            ],
            options={
                'db_table': 'Departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'Education',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Familyrelationships',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('titularid', models.IntegerField(db_column='TitularId', null=True)),
                ('beneficiaryid', models.IntegerField(db_column='BeneficiaryId', null=True)),
                ('relationship', models.CharField(db_column='Relationship', max_length=50)),
            ],
            options={
                'db_table': 'FamilyRelationships',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Healthaffiliationtype',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'HealthAffiliationType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Identificationtype',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50)),
            ],
            options={
                'db_table': 'IdentificationType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('code', models.CharField(db_column='Code', max_length=100)),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('active', models.BooleanField(db_column='Active', default=True, null=True)),
            ],
            options={
                'db_table': 'Municipalities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
            ],
            options={
                'db_table': 'Occupation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productiveline',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'ProductiveLine',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subjectofspecialprotection',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'SubjectOfSpecialProtection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Township',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'Township',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserPNIS',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=255, null=True)),
                ('identificationnumber', models.CharField(blank=True, db_column='IdentificationNumber', max_length=50, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=50, null=True)),
                ('sexualorientation', models.CharField(blank=True, db_column='SexualOrientation', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'Village',
                'managed': False,
            },
        ),
    ]
