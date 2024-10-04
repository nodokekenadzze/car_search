from rest_framework import serializers
from .models import Make, Model, CarType

class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = '__all__'
