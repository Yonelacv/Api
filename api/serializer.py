from rest_framework import serializers
from .models import Interacciones

class InteraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interacciones
        fields = '__all__'