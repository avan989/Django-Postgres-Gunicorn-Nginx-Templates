from rest_framework import serializers
from .models import ApprenticeshipDevelop


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprenticeshipDevelop
        fields = ('title', 'description', 'image', 'url')
