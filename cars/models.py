# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.timezone import now

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


#05/01 add user and admin
class LxyUser(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
class LxyAdmin(models.Model):
    adminname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    

class LxyClass(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=20)
    class_dailyrate = models.DecimalField(max_digits=6, decimal_places=2)
    class_over_m_fee = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'lxy_class'
    


# class LxyCredit(models.Model):
#     paym_numb = models.ForeignKey('LxyPayment', models.DO_NOTHING, db_column='paym_numb',related_name='credit_payment_fk')#0429zengjia relatedname
#     paym_type = models.OneToOneField('LxyPayment', models.DO_NOTHING, db_column='paym_type', primary_key=True)
#     cred_numb = models.BigIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'lxy_credit'
#         unique_together = (('paym_type', 'paym_numb'),)


class LxyCustCorp(models.Model):
    cust = models.OneToOneField('LxyCustomer', models.DO_NOTHING, primary_key=True)
    corp_reginum = models.CharField(max_length=20)
    corp_eid = models.CharField(max_length=20)
    corp_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'lxy_cust_corp'
        unique_together = (('corp_reginum', 'corp_eid'),)


class LxyCustIndi(models.Model):
    cust = models.OneToOneField('LxyCustomer', models.DO_NOTHING, primary_key=True)
    indi_dln = models.CharField(unique=True, max_length=13)
    indi_fname = models.CharField(max_length=20)
    indi_mname = models.CharField(max_length=20, blank=True, null=True)
    indi_lname = models.CharField(max_length=20)
    indi_icn = models.CharField(max_length=50)
    indi_ipn = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'lxy_cust_indi'


class LxyCustomer(models.Model):
    #cust_id=models.IntegerField(primary_key=True)
    cust_id=models.AutoField(primary_key=True)
    cust_username=models.CharField(max_length=50)#05/09 add
    cust_password=models.CharField(max_length=50)#05/09 add
    #cust_id = models.BigIntegerField(primary_key=True)
    cust_street = models.CharField(max_length=30)
    cust_city = models.CharField(max_length=20)
    cust_state = models.CharField(max_length=20)
    cust_zip = models.IntegerField()
    cust_email = models.CharField(max_length=30)
    cust_phone = models.BigIntegerField()
    #cust_type = models.CharField(max_length=2)
    #disc_numb = models.OneToOneField('LxyDiscount', models.DO_NOTHING,db_column='disc_numb')
    disc_numb=models.CharField(default='0',max_length=20)

    def __str__(self):
        return self.cust_username

    class Meta:
        managed = False
        db_table = 'lxy_customer'


# class LxyDebit(models.Model):
#     paym_numb = models.ForeignKey('LxyPayment', models.DO_NOTHING, db_column='paym_numb',related_name='debit_payment_fk')#0429zengjia related_name
#     paym_type = models.OneToOneField('LxyPayment', models.DO_NOTHING, db_column='paym_type', primary_key=True)
#     debi_numb = models.BigIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'lxy_debit'
#         unique_together = (('paym_type', 'paym_numb'),)


# class LxyDiscCorp(models.Model):
#     disc_numb = models.OneToOneField('LxyDiscount', models.DO_NOTHING, db_column='disc_numb', primary_key=True)
#     disc_corp_sdate = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'lxy_disc_corp'


# class LxyDiscIndi(models.Model):
#     disc_numb = models.OneToOneField('LxyDiscount', models.DO_NOTHING, db_column='disc_numb', primary_key=True)
#     disc_indi_sdate = models.DateTimeField()
#     disc_indi_edate = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'lxy_disc_indi'


# class LxyDiscount(models.Model):
#     disc_numb = models.CharField(primary_key=True, max_length=10)
#     #disc_numb = models.BigAutoField(primary_key=True)
#     disc_rate = models.DecimalField(default=1,max_digits=4, decimal_places=2)
#     disc_type = models.CharField(max_length=2)

#     class Meta:
#         managed = False
#         db_table = 'lxy_discount'


# class LxyGift(models.Model):
#     paym_numb = models.ForeignKey('LxyPayment', models.DO_NOTHING, db_column='paym_numb',related_name='gift_payment_fk')#0429 add related_name
#     paym_type = models.OneToOneField('LxyPayment', models.DO_NOTHING, db_column='paym_type', primary_key=True)
#     gift_numb = models.BigIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'lxy_gift'
#         unique_together = (('paym_type', 'paym_numb'),)


# class LxyInvoice(models.Model):
#     invo_numb = models.BigIntegerField(primary_key=True)
#     invo_date = models.DateTimeField(default=now)
#     invo_amou = models.DecimalField(max_digits=7, decimal_places=2)
#     invo_payed = models.CharField(default=0,max_length=2000)
#     serv_numb = models.OneToOneField('LxyRentServ', models.DO_NOTHING, db_column='serv_numb')

#     class Meta:
#         managed = False
#         db_table = 'lxy_invoice'


class LxyOffice(models.Model):
    offi_id = models.SmallIntegerField(primary_key=True)
    offi_street = models.CharField(max_length=50)
    offi_city = models.CharField(max_length=20)
    offi_state = models.CharField(max_length=20)
    offi_zip = models.IntegerField()
    offi_phone = models.BigIntegerField()

    def __str__(self):
        return self.offi_city

    class Meta:
        managed = False
        db_table = 'lxy_office'


# class LxyPayment(models.Model):
#     paym_numb = models.BigIntegerField()
#     paym_type = models.CharField(primary_key=True, max_length=2)
#     paym_amou = models.DecimalField(max_digits=7, decimal_places=2)
#     paym_date = models.DateTimeField()
#     invo_numb = models.ForeignKey(LxyInvoice, models.DO_NOTHING, db_column='invo_numb')

#     class Meta:
#         managed = False
#         db_table = 'lxy_payment'
#         unique_together = (('paym_type', 'paym_numb'),)


class LxyRentServ(models.Model):
    serv_numb = models.BigIntegerField(primary_key=True)
    pick_offi = models.ForeignKey(LxyOffice, models.DO_NOTHING,related_name='pick_fk')#0429 add related_name
    drop_offi = models.ForeignKey(LxyOffice, models.DO_NOTHING,related_name='drop_fk')#0429 add related_name
    pick_date = models.DateTimeField()
    drop_date = models.DateTimeField(default=now)
    sodom = models.IntegerField()
    eodom = models.IntegerField(default=0)
    dail_limi = models.SmallIntegerField(default=5)
    unlimi = models.CharField(default='no',max_length=2000)
    vehi_lice = models.ForeignKey('LxyVehicle', models.DO_NOTHING, db_column='vehi_lice')
    cust = models.ForeignKey(LxyCustomer, models.DO_NOTHING)
    #05/11/2022
    payment=models.FloatField(default=0)

    def __str__(self):
        return self.cust.cust_username

    class Meta:
        managed = False
        db_table = 'lxy_rent_serv'


class LxyVehicle(models.Model):
    vehi_lice = models.CharField(primary_key=True, max_length=8)
    vehi_vin = models.CharField(max_length=17)
    vehi_make = models.CharField(max_length=20)
    vehi_model = models.CharField(max_length=20)
    vehi_year = models.SmallIntegerField()
    class_field = models.ForeignKey(LxyClass, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    offi = models.ForeignKey(LxyOffice, models.DO_NOTHING)

    def __str__(self):
        return self.vehi_model
    class Meta:
        managed = False
        db_table = 'lxy_vehicle'
