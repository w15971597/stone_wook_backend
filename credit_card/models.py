from django.db import models

# Create your models here.


class BillTab(models.Model):
	card_no = models.CharField(max_length=64)
	type = models.SmallIntegerField(default=0)
	category = models.CharField(max_length=64)
	merchant = models.CharField(max_length=256)
	amount = models.IntegerField(default=0)
	status = models.SmallIntegerField(default=0)
	ctime = models.IntegerField(default=0)
	mtime = models.IntegerField(default=0)

	class Meta:
		db_table = 'bill_tab'
		app_label = 'model'


class CardTab(models.Model):
	bank = models.CharField(max_length=64)
	logo = models.CharField(max_length=256)
	card_no = models.CharField(max_length=64)
	holder = models.CharField(max_length=64)
	total = models.IntegerField(default=0)
	available = models.IntegerField(default=0)
	remark = models.CharField(max_length=256)
	status = models.SmallIntegerField()

	cost_day = models.IntegerField(default=0)
	pay_day = models.IntegerField(default=0)
	ctime = models.IntegerField(default=0)
	mtime = models.IntegerField(default=0)

	class Meta:
		db_table = 'card_tab'
		app_label = 'model'


class FeedbackTab(models.Model):
	username = models.CharField(max_length=64)
	phone = models.CharField(max_length=256)
	remark = models.CharField(max_length=256)
	status = models.SmallIntegerField(default=0)

	ctime = models.IntegerField(default=0)
	mtime = models.IntegerField(default=0)

	class Meta:
		db_table = 'feedback_tab'
		app_label = 'model'


class UserTab(models.Model):
	username = models.CharField(max_length=64)
	password = models.CharField(max_length=64)
	phone = models.CharField(max_length=256)
	status = models.SmallIntegerField(default=0)

	ctime = models.IntegerField(default=0)
	mtime = models.IntegerField(default=0)

	class Meta:
		db_table = 'user_tab'
		app_label = 'model'
