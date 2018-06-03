from rest_framework import serializers

from website.models import *


class EventSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Events
		fields = [
			'pk',
			'url',
			'usrid',
			'title',
			'desc',
			'edate',
			'target_fund',
			'status',
			'visibleto',
			'date_created'
		]

		read_only_fields = ['usrid','date_created']


	def get_url(self, obj):
		request = self.context.get("request")
		return obj.get_api_url(request=request)


	#Sample Validation (example: if you want to make title as unique)
	#def validate(self, value): #for every fields
	def validate_title(self, value): #for title only
		qs = Events.objects.filter(title__iexact=value) #including the whole instance
		if self.intance:
			qs = qs.exlude(pk=self.instance.pk)
		if qs.exist():
			raise serializers.ValidationError("Event Exist and must be unique")
		return value