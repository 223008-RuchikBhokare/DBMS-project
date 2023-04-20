# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Normdoctors(models.Model):
    doc_id = models.IntegerField(primary_key=True)
    doc_name = models.CharField(max_length=20, blank=True, null=True)
    doc_age = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    specialization = models.CharField(max_length=20, blank=True, null=True)
    normdoctorscol1 = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    mr_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normdoctors'


class Normmedrec(models.Model):
    mr_no = models.IntegerField(db_column='MR_No', primary_key=True)  # Field name made lowercase.
    treatment = models.CharField(db_column='Treatment', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wbc_count = models.IntegerField(db_column='WBC_Count', blank=True, null=True)  # Field name made lowercase.
    blood_group = models.CharField(db_column='Blood_Group', max_length=10, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='Doc_ID', blank=True, null=True)  # Field name made lowercase.
    patient_id = models.IntegerField(db_column='Patient_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'normmedrec'


class Normpatients(models.Model):
    patient_id = models.IntegerField(db_column='Patient_ID', primary_key=True)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.FloatField(db_column='Phone_No', blank=True, null=True)  # Field name made lowercase.
    room_id = models.IntegerField(db_column='Room_ID', blank=True, null=True)  # Field name made lowercase.
    reg_id = models.IntegerField(db_column='Reg_ID', blank=True, null=True)  # Field name made lowercase.
    pres_id = models.IntegerField(db_column='Pres_ID', blank=True, null=True)  # Field name made lowercase.
    bill_id = models.IntegerField(db_column='Bill_ID', blank=True, null=True)  # Field name made lowercase.
    mr_no = models.IntegerField(db_column='MR_No', blank=True, null=True)  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='Doc_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'normpatients'
