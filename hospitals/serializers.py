from rest_framework import serializers
from .models import HospitalRecord
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalRecord
        fields = '__all__'