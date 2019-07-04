# Generated by Django 2.0.6 on 2019-07-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TPersonalInformation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.CharField(blank=True, max_length=255, null=True)),
                ('salary', models.CharField(blank=True, max_length=255, null=True)),
                ('jobsite', models.CharField(blank=True, max_length=255, null=True)),
                ('native_place', models.CharField(blank=True, max_length=255, null=True)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('specialty', models.CharField(blank=True, max_length=255, null=True)),
                ('work_experience', models.CharField(blank=True, max_length=255, null=True)),
                ('current_address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('job_wanted', models.CharField(blank=True, max_length=255, null=True)),
                ('expect_vocation', models.CharField(blank=True, max_length=255, null=True)),
                ('expect_job', models.CharField(blank=True, max_length=255, null=True)),
                ('guojia', models.CharField(blank=True, max_length=255, null=True)),
                ('politics_status', models.CharField(blank=True, max_length=255, null=True)),
                ('matrimony', models.CharField(blank=True, max_length=255, null=True)),
                ('job_nature', models.CharField(blank=True, max_length=255, null=True)),
                ('education_experience', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_personal_information',
            },
        ),
        migrations.CreateModel(
            name='TTeacher',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.CharField(blank=True, max_length=255, null=True)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('work_experience', models.CharField(blank=True, max_length=255, null=True)),
                ('expect_job', models.CharField(blank=True, max_length=255, null=True)),
                ('expect_vocation', models.CharField(blank=True, max_length=255, null=True)),
                ('salary', models.CharField(blank=True, max_length=255, null=True)),
                ('jobsite', models.CharField(blank=True, max_length=255, null=True)),
                ('job_wanted', models.CharField(blank=True, max_length=255, null=True)),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('specialty', models.CharField(blank=True, max_length=255, null=True)),
                ('education_experience', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_teacher',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('pass_field', models.CharField(db_column='pass', max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 't_user',
            },
        ),
        migrations.CreateModel(
            name='TWangxingPersonal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('userid', models.CharField(blank=True, db_column='userID', max_length=255, null=True)),
                ('sex', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.CharField(blank=True, max_length=255, null=True)),
                ('home', models.CharField(blank=True, max_length=255, null=True)),
                ('work_experience', models.CharField(blank=True, max_length=255, null=True)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('jobsite', models.CharField(blank=True, max_length=255, null=True)),
                ('expect_job', models.CharField(blank=True, max_length=255, null=True)),
                ('salary', models.CharField(blank=True, max_length=255, null=True)),
                ('job_nature', models.CharField(blank=True, max_length=255, null=True)),
                ('job_wanted', models.CharField(blank=True, max_length=255, null=True)),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('specialty', models.CharField(blank=True, max_length=255, null=True)),
                ('education_experience', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_wangxing_personal',
            },
        ),
    ]
