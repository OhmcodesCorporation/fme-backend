from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
		HTTP_200_OK,
		HTTP_400_BAD_REQUEST,
	)



from website.models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly

class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserDetailAPIView(generics.ListAPIView):
	permission_classes = [IsAdminUser]
	serializer_class = UserDetailSerializer

	def get_queryset(self):
		qs = User.objects.all()
		return qs

class UserCreateAPIView(generics.CreateAPIView):
	permission_classes = [AllowAny]
	serializer_class = UserCreateSerializer
	qs = User.objects.all()

class EventsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = EventSerializer

	def get_queryset(self):
		qs = Events.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter( Q(title__icontains=query) | Q(desc__icontains=query) ).distinct()
		return qs

	def perform_create(self, serializer):
		serializer.save(usrid=self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	# def put(self, request, *args, **kwargs):
	# 	return self.update(request, *args, **kwargs)

	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}

	# def patch(self, request, *args, **kwargs):
	# 	return self.update(request, *args, **kwargs)

class EventsRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = EventSerializer
	permission_classes = [IsOwnerOrReadOnly]

	def get_queryset(self):
		return Events.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}
