from django.contrib import admin

from django.contrib.admin import AdminSite

# Register your models here.
from .models import *


site_header = 'FME Backend'

# class ProfileAdmin(admin.ModelAdmin):

# 	class Meta:
# 		model = Profile
		
	
# 	#fields = ['fnme','usrn']
# 	#exclude = ['pwd']
# 	#list_display = ('fullname', 'usr', 'eml', 'date_registered', 'action_buttons')
		

# admin.site.register(Profile, ProfileAdmin)
