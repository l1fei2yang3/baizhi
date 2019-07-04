# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TPersonalInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    jobsite = models.CharField(max_length=255, blank=True, null=True)
    native_place = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    work_experience = models.CharField(max_length=255, blank=True, null=True)
    current_address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    job_wanted = models.CharField(max_length=255, blank=True, null=True)
    expect_vocation = models.CharField(max_length=255, blank=True, null=True)
    expect_job = models.CharField(max_length=255, blank=True, null=True)
    guojia = models.CharField(max_length=255, blank=True, null=True)
    politics_status = models.CharField(max_length=255, blank=True, null=True)
    matrimony = models.CharField(max_length=255, blank=True, null=True)
    job_nature = models.CharField(max_length=255, blank=True, null=True)
    education_experience = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_personal_information'


class TTeacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    work_experience = models.CharField(max_length=255, blank=True, null=True)
    expect_job = models.CharField(max_length=255, blank=True, null=True)
    expect_vocation = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    jobsite = models.CharField(max_length=255, blank=True, null=True)
    job_wanted = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    education_experience = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_teacher'


class TUser(models.Model):
    username = models.CharField(max_length=255)
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 't_user'


class TWangxingPersonal(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    userid = models.CharField(db_column='userID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    home = models.CharField(max_length=255, blank=True, null=True)
    work_experience = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    jobsite = models.CharField(max_length=255, blank=True, null=True)
    expect_job = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    job_nature = models.CharField(max_length=255, blank=True, null=True)
    job_wanted = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    education_experience = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_wangxing_personal'
