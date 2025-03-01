from rest_framework import serializers
from .models import *

class RingSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RingSettings
        fields = '__all__'
