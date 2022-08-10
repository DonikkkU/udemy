from rest_framework import status

from .models import Profiles
from .serializers import ProfilesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

@api_view(['GET', 'POST'])
def profiles(request):
    if request.method == 'GET':
        profiles = Profiles.objects.all()
        serializer = ProfilesSerializer(profiles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk):
    try:
        profile = Profiles.objects.get(pk=pk)
    except Profiles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfilesSerializer(profiles)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfilesSerializer(profiles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
