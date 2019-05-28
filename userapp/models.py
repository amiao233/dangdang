# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAdd(models.Model):
    add_id = models.CharField(primary_key=True, max_length=20)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    addr = models.CharField(max_length=20, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_add'


class TBook(models.Model):
    book_id = models.CharField(primary_key=True, max_length=20)
    writer = models.CharField(max_length=64, blank=True, null=True)
    press = models.CharField(max_length=128, blank=True, null=True)
    publicaion_time = models.DateField(blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)
    printing_time = models.CharField(max_length=20, blank=True, null=True)
    impression = models.CharField(max_length=20, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=64, blank=True, null=True)  # Field name made lowercase.
    words = models.CharField(max_length=64, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    paper = models.CharField(max_length=64, blank=True, null=True)
    package = models.CharField(max_length=64, blank=True, null=True)
    class2 = models.ForeignKey('TUser2', models.DO_NOTHING, blank=True, null=True)
    book_name = models.CharField(max_length=128, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    dprice = models.IntegerField(blank=True, null=True)
    recommed = models.CharField(max_length=2000, blank=True, null=True)
    content_introduction = models.CharField(max_length=2000, blank=True, null=True)
    author_introduction = models.CharField(max_length=2000, blank=True, null=True)
    menu = models.CharField(max_length=2000, blank=True, null=True)
    review = models.CharField(max_length=2000, blank=True, null=True)
    image = models.CharField(max_length=2000, blank=True, null=True)
    image_path = models.CharField(max_length=2000, blank=True, null=True)
    serise_name = models.CharField(max_length=128, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    shelves_date = models.DateField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    book_status = models.IntegerField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TClass(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    class_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_class'


class TOrder(models.Model):
    ord_id = models.CharField(primary_key=True, max_length=20)
    create_date = models.DateField(blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)
    add = models.ForeignKey(TAdd, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TUser(models.Model):
    user_email = models.CharField(max_length=20, blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    user_password = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.CharField(primary_key=True, max_length=20)
    user_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class TUser2(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    class_name = models.CharField(max_length=20, blank=True, null=True)
    class1 = models.ForeignKey(TClass, models.DO_NOTHING, blank=True, null=True)
    counts = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user2'


class TVerify(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    product_number = models.CharField(max_length=20, blank=True, null=True)
    subtotal = models.CharField(max_length=20, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    ord = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_verify'


class Confirm_string(models.Model):
    code = models.CharField(max_length=256, verbose_name='用户注册码')
    user = models.ForeignKey('TUser', on_delete=models.CASCADE, verbose_name='关联的用户')
    code_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 't_confirm_string'


