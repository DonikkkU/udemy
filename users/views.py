
from .models import Profiles
from .serializers import *
from rest_framework import generics

class ProfilesView(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer

class ProfilesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
