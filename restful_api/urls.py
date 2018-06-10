from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import *

urlpatterns = [
	url(r'^token/auth/$', obtain_jwt_token),
	url(r'^token/refresh/$', refresh_jwt_token),
	url(r'^token/verify/$', verify_jwt_token),
	url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
	url(r'^members/$', UserDetailAPIView.as_view(), name='members'),
	url(r'^events/$', EventsAPIView.as_view(), name='events-create'),
	url(r'^events/(?P<pk>\d+)/$', EventsRUDView.as_view(), name='events-rud'),
	url(r'^wishlist/$', WishlistAPIView.as_view(), name='wish-create'),
	url(r'^wishlist/(?P<pk>\d+)/$', WishlistRUDView.as_view(), name='wish-rud'),
]


'''

Run curl in terminal
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser6","password":"testuser69"}' http://localhost:8000/api/token/auth/

Sample Response
{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4LCJ1c2VybmFtZSI6InRlc3R1c2VyNiIsImV4cCI6MTUyODA2NzY0NiwiZW1haWwiOiJ0ZXN0NkB0ZXN0LmNvbSJ9.vhGG53DAvpfPTtxp7wmHhd-6E7S5FHsFxIROsTP3Njk"}


curl -H "Authorization: JWT <your_token>" http://localhost:8000/api/events/

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo4LCJ1c2VybmFtZSI6InRlc3R1c2VyNiIsImV4cCI6MTUyODA2NzY0NiwiZW1haWwiOiJ0ZXN0NkB0ZXN0LmNvbSJ9.vhGG53DAvpfPTtxp7wmHhd-6E7S5FHsFxIROsTP3Njk" http://localhost:8000/api/events/



'''