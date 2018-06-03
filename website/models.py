from django.db import models

from django.urls import reverse

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth.models import User

import datetime,os
from decimal import Decimal

from rest_framework.reverse import reverse as api_reverse
#django host lib for url with subdomain for reverse


# Create your models here.


#Path for User Images
def GetPath(intance,filename):
	return os.path.join( settings.USER_URL, str(intance.id), str(filename) )

class DetailedProfile(models.Model):
	usrid = models.ForeignKey(User, null=True,verbose_name='User',on_delete=models.CASCADE)
	int_eml = models.EmailField(max_length=50, null=True, default='default@fme.com',verbose_name='Interact Email Address')
	address = models.TextField(null=True,blank=True,verbose_name='Address')
	province = models.CharField(max_length=100,null=True,blank=True,verbose_name='Province')
	postalcode = models.CharField(max_length=20,null=True,blank=True,verbose_name='Postalcode')
	cp = models.CharField(max_length=100,null=True,blank=True,verbose_name='Cellphone')
	landline = models.CharField(max_length=100,null=True,blank=True,verbose_name='Landline')
	usr_img = models.ImageField(upload_to=GetPath, blank=True, null=True,verbose_name='Profile Image')
	#Public/Private (if private cant see you in public user or search people)
	CHOICES_PRIVACY = (
	     ('pub', 'Public'),
	     ('pri', 'Private'),
	)
	privacy = models.CharField(max_length=3000, default='pub', choices=CHOICES_PRIVACY, verbose_name='Privacy')

class UserFriends(models.Model):
	usrid = models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE,related_name="userfriends_usrid_set")
	friend = models.ForeignKey(User,verbose_name='Friend',on_delete=models.CASCADE, related_name="userfriends_friend_set")
	#Friend/Family/Acquaintance
	CHOICES_FTYPE = (
	     ('fri', 'Friend'),
	     ('fam', 'Family'),
	     ('acq', 'Acquaintances'),
	)
	ftype = models.CharField(max_length=100, default='fri', choices=CHOICES_FTYPE, verbose_name='Friend Type')
	date_added = models.DateTimeField(("Friend Since"), default=timezone.now)

class Events(models.Model):
	usrid = models.ForeignKey(User,verbose_name='User ID',on_delete=models.CASCADE)
	title = models.CharField(max_length=300,verbose_name='Title')
	desc = models.CharField(max_length=3000,null=True,blank=True,verbose_name='Description')
	edate = models.DateTimeField(("Date"), default=timezone.now)
	target_fund = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'),verbose_name='Target')
	#On Going/Passed/Incoming
	CHOICES_ESTATUS = (
	     ('ong', 'On Going'),
	     ('pas', 'Passed'),
	     ('inc', 'Incoming'),
	)
	status = models.CharField(max_length=100, default='pub', choices=CHOICES_ESTATUS, verbose_name='Status')
	#Only Friends/Public
	CHOICES_VISIBLE = (
		 ('all', 'All'),
	     ('fri', 'Only Friends'),
	     ('fam', 'Family'),
	     ('acq', 'Acquaintances')
	)
	visibleto = models.CharField(max_length=100, default='public', choices=CHOICES_VISIBLE, verbose_name='Visible To')
	date_created = models.DateTimeField(("Date Created"), default=timezone.now)

	def __str__(self):
		return self.title
	title.short_description = "Event Title"

	@property
	def owner(self):
		return self.usrid

	#to get url in api request
	def get_api_url(self, request=None):
		return api_reverse("api-world:events-rud", kwargs={'pk':self.pk},request=request)
	

class Wishlist(models.Model):
	eid = models.ForeignKey(Events,verbose_name='Event', related_name='wishlist',on_delete=models.CASCADE)
	name = models.CharField(max_length=300,verbose_name='Wish')
	desc = models.CharField(max_length=3000,null=True,blank=True,verbose_name='Description')
	message = models.CharField(max_length=3000,null=True,blank=True,verbose_name='Message')
	alotted = models.DecimalField(blank=True, max_digits=20, decimal_places=2, default=Decimal('0.00'),verbose_name='Alotted')
	prod_link = models.URLField(max_length=200,null=True,blank=True,verbose_name='Url')
	price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('1.00'),verbose_name='Price')
	date_created = models.DateTimeField(("Date Created"), default=timezone.now)

	def __str__(self):
		return self.name


class EventInvitees(models.Model):
	eid = models.ForeignKey(Events,verbose_name='Event',on_delete=models.CASCADE)
	usrid = models.ForeignKey(User,verbose_name='User ID',on_delete=models.CASCADE)
	#Coming/Maybe/Next time
	CHOICES_EPRIVACY = (
	     ('cm', 'Coming'),
	     ('mb', 'Maybe'),
	     ('nt', 'Next Time')
	)
	status = models.CharField(max_length=100, default='cm', choices=CHOICES_EPRIVACY, verbose_name='Status')
	date_invited = models.DateTimeField(("Date Invited"), default=timezone.now)

# class UserWallPosts(models.Model):

# class WallThread(models.Model):

# class EventThread(models.Model):

# class WishThread(models.Model):

# class Notifications(models.Model):
# 	usrid = models.ForeignKey(User,verbose_name='User ID',on_delete=models.CASCADE)
# 	msg = models.CharField(max_length=100,null=True,blank=True,verbose_name='Province')
# 	#Event Incoming/Fund raised/Target reach or near/Friend stuff(added,invite, invite confirmation)/ads
# 	# CHOICES_EPRIVACY = (
# 	#      ('p', 'Peding'),
# 	#      ('d', 'Done'),
# 	# )
# 	# types = models.CharField(max_length=100, default='p', choices=CHOICES_SNOTIF, verbose_name='Type')
# 	#pending/done
# 	CHOICES_SNOTIF = (
# 	     ('p', 'Peding'),
# 	     ('d', 'Done'),
# 	)
# 	status = models.CharField(max_length=100, default='p', choices=CHOICES_SNOTIF, verbose_name='Status')
# 	date_performed = models.DateTimeField(("Date perfomed"), default=timezone.now)










	# #Admin Table
	# def fullname(self):
	# 	return self.fnme + ' ' + self.mnme + ' ' + self.lnme
	# fullname.short_description = "Full name"

	# #defining objects on foreign key rely on dropdown ADMIN
	# def __str__(self):
	# 	return self.fnme + ' ' + self.mnme + ' ' + self.lnme

	# def usr(self):
	# 	return self.usrn
	# usr.short_description = "Username"

	# def eml(self):
	# 	return self.emladdress
	# eml.short_description = "Email Address"

	# def date_registered(self):
	# 	return self.regdate
	# date_registered.short_description = "Date Registered"

	# def action_buttons(self):
	# 	return format_html(
	# 		'<a class="btn" href="/admin/profiles/profile/{}/change/">Change</a> | '+
	# 		'<a class="btn" href="/admin/profiles/profile/{}/delete/">Delete</a>',
	# 		self.mid, self.mid, self.mid)
	# action_buttons.short_description = "Actions"
