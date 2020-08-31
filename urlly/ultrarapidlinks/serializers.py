from .models import StoredURL
from rest_framework import serializers

class StoredURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoredURL
        fields = ['descriptor', 'url', 'counter', 'created']
