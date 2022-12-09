from rest_framework import serializers
from .models import ImmigrationStatusData, CategoryData, CountryData, DestinationData

class ImmigrationStatusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImmigrationStatusData
        fields = "__all__"

class CategoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryData
        fields = "__all__"

class CountryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryData
        fields = "__all__"

class DestinationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationData
        fields = "__all__"

