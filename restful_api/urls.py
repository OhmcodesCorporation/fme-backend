from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
	url(r'^events/$', EventsAPIView.as_view(), name='events-create'),
	url(r'^events/(?P<pk>\d+)/$', EventsRUDView.as_view(), name='events-rud'),
]