from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^events/$', EventsAPIView.as_view(), name='events-create'),
	url(r'^events/(?P<pk>\d+)/$', EventsRUDView.as_view(), name='events-rud'),
]