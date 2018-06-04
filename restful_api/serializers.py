from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.serializers import (
	CharField,
	EmailField,
	StringRelatedField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)

from website.models import *



class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField(required=False, allow_blank=True, label="Username/Email")
	#email = EmailField(label="Email Address", required=False, allow_blank=True)
	password = CharField(style={'input_type':'password'}, write_only=True)
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'token',
		]
		extra_kwargs = {"password":{"write_only": True}}

	def validate(self, data):
		usrobj = None
		email = data.get("email", None)
		username = data.get("username", None)
		password = data["password"]
		if not username:
			raise ValidationError("A username or email are required to login.")

		user = User.objects.filter(
				Q(email=username) |
				Q(username=username)
			).distinct()
		#if registered user doesnt have emails
		user = user.exclude(email__isnull=True).exclude(email__iexact='')
		if user.exists() and user.count() == 1:
			usrobj = user.first()
		else:
			raise ValidationError("This username/email is not valid.")

		if usrobj:
			if not usrobj.check_password(password):
				raise ValidationError("Incorrect Password.")

		data["username"] = usrobj.username #Overide username response if email used for login

		data["token"] = "RANDOM TOKEN"

		return data

class UserDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name'
		]

class UserCreateSerializer(ModelSerializer):
	email = EmailField() #to be required field
	password = CharField(style={'input_type':'password'}, write_only=True)
	password2 = CharField(label="Confirm Password", style={'input_type':"password"}, write_only=True)
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'password2',
			'email',
		]
		extra_kwargs = {"password":{"write_only": True}}

	# def validate(self, data):
	# 	# email = data['email']
	# 	# user_qs = User.objects.filter(email=email)
	# 	# if user_qs.exists():
	# 	# 	raise ValidationError("This email has already registered")
	# 	# return data
	# 	if not data.get('password') or not data.get('password2'):
	# 		raise ValidationError("Please enter a password and confirm it.")

	# 	if data.get('password') != data.get('password2'):
	# 		raise ValidationError("Passwords didn't match.")

	# 	return data


	def validate_email(self, value):
		data = self.get_initial()
		email = data.get("email")
		user_qs = User.objects.filter(email=email)
		if user_qs.exists():
			raise ValidationError("This email has already registered")
		return value

	def validate_password(self, value):
		data = self.get_initial()
		password = data.get("password2")
		password2 = value

		if password != password2:
			raise ValidationError("Password Doesn't match.")

		return value

	def validate_password2(self, value):
		data = self.get_initial()
		password = data.get("password")
		password2 = value

		if password != password2:
			raise ValidationError("Password Doesn't match.")

		return value

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		email = validated_data['email']
		usrobj = User(username = username, email = email)
		usrobj.set_password(password)
		usrobj.save()
		return validated_data

class WishlistSerializer(ModelSerializer):
	class Meta:
		model = Wishlist
		fields = [
			'name',
			'desc',
			'allotted',
			'prod_link',
			'price',
			'date_created',
		]

class EventSerializer(ModelSerializer):
	url = SerializerMethodField(read_only=True)
	usrid = UserDetailSerializer(read_only=True)
	wishlist = StringRelatedField(many=True, read_only=True) #get wishlist related to Event
	wl_count = SerializerMethodField() #get wishlist count to related Event
	class Meta:
		model = Events
		fields = [
			'pk',
			'url',
			'title',
			'desc',
			'edate',
			'target_fund',
			'status',
			'visibleto',
			'date_created',
			'usrid',
			'wishlist',
			'wl_count'
		]

		read_only_fields = ['usrid','date_created', 'wishlist', 'wl_count']

	# def get_wl(self, obj):
	# 	return WishlistSerializer(obj, many=True).data

	def get_wl_count(self, obj):
		return Wishlist.objects.filter(eid=obj).count()

	def get_url(self, obj):
		request = self.context.get("request")
		return obj.get_api_url(request=request)


	#Sample Validation (example: if you want to make title as unique)
	#def validate(self, value): #for every fields
	def validate_title(self, value): #for title only
		qs = Events.objects.filter(title__iexact=value) #including the whole instance
		if self.instance:
			qs = qs.exlude(pk=self.instance.pk)
		if qs.exists():
			raise ValidationError("Event Exist and must be unique")
		return value



