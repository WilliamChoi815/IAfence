from rest_framework import serializers
from .models import Match

#DB --> JSON
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'