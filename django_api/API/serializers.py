from rest_framework import serializers
from .models import UserProfile, ArticleCars, CarModel, FuelType

# public endpoint to serve data from your models with all related objects

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ArticleCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCars
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['data_posted'] = instance.data_posted.strftime('%d-%m-%Y %H:%M:%S')
        return representation

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'




