from django.db.models import Q
from rest_framework import generics, mixins
from website.models import *
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer



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
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

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