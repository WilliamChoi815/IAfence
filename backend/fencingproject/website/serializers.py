from rest_framework import serializers
from .models import Match, Player, Player_Point, Tournament, Tournament_Bracket, Tournament_Player

#DB --> JSON
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PlayerPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player_Point
        fields = '__all__'
        
class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class TournamentBracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament_Bracket
        fields = '__all__'

class TournamentPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament_Player
        fields = '__all__'