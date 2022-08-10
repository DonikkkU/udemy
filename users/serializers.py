from rest_framework import serializers
from .models import *

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'full_name', 'ROLE', ]