from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from profiles.models import Profile, Financial
from django.core.exceptions import NON_FIELD_ERRORS

class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    # last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    # user_name = forms.CharField(max_length=30, required=True, help_text='Required')
    # email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1' )

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['emailaddress1','mnme','address1','address2', 'billing_address', 'shipping_address', 'dob', 'country','title', 'province',
#                      'postalcode', 'cp', 'landline', 'timezone', 'facebook', 'twitter', 'insta', 'webaddress', 'profile_type',
#                      'business_name', 'slogan']
#         widgets = {
#             'address1': forms.Textarea(attrs={'class':'materialize-textarea'}),
#             'address2': forms.Textarea(attrs={'class':'materialize-textarea'}),
#             'billing_address': forms.Textarea(attrs={'class':'materialize-textarea'}),
#             'shipping_address': forms.Textarea(attrs={'class':'materialize-textarea'}),
#             'dob': forms.DateInput(attrs={'class':'datepicker'}),
#         }
    
class contactUsForm(forms.Form):
	subject = forms.CharField(required= True)
	email = forms.EmailField(required = True)
	message = forms.CharField(required = True, widget = forms.Textarea(attrs={'class' : 'materialize-textarea'}))