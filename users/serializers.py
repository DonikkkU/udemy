from rest_framework import serializers
from .models import *
from projects.models import *

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ['full_name', 'user', 'ROLE', 'image', 'about']