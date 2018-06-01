from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from .views import *


urlpatterns = [
	url(r'^$', HomeView.as_view(), name='index' ),
	url(r'^aboutus/$', AboutView.as_view(), name='about' ),
	url(r'^contactus/$', views.contactus, name='contact' ),
	url(r'^thanks/$', ThanksView.as_view(), name='thanks' ),
	url(r'^profile/$', views.ProfileView, name='profile' ),
	url(r'^signup/$', views.CreateUser, name='signuppage' ),
    url(r'^login/$', auth_views.login, name='login' ),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout' ),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
	url(r'^', include('django.contrib.auth.urls')),
	url(r'^oauth/', include('social_django.urls', namespace='social')), # for social login
]

