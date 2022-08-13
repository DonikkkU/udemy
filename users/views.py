
from .models import Profiles
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class ProfilesView(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer


class ProfilesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    filterset_fields = '__all__'
    search_fields = ['-full_name']
    ordering_fields = '__all__'
