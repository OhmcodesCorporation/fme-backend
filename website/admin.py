from django.contrib import admin

from django.contrib.admin import AdminSite

# Register your models here.
from .models import *


site_header = 'FME Backend'

class DetailedProfileAdmin(admin.ModelAdmin):

	class Meta:
		model = DetailedProfile
		
	#fields = ['fnme','usrn']
	#exclude = ['prod_regdate']
	#ist_display = ('prod_name',)
	

admin.site.register(DetailedProfile, DetailedProfileAdmin)


class UserFriendsAdmin(admin.ModelAdmin):

	class Meta:
		model = UserFriends

admin.site.register(UserFriends, UserFriendsAdmin)


class EventsAdmin(admin.ModelAdmin):

	class Meta:
		model = Events

admin.site.register(Events, EventsAdmin)


class WishlistAdmin(admin.ModelAdmin):

	class Meta:
		model = Wishlist

admin.site.register(Wishlist, WishlistAdmin)


class EventInviteesAdmin(admin.ModelAdmin):

	class Meta:
		model = EventInvitees

admin.site.register(EventInvitees, EventInviteesAdmin)
