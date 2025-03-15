from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Match, Player, Player_Point, Tournament, Tournament_Bracket, Tournament_Player
from .serializers import MatchSerializer, PlayerSerializer, PlayerPointSerializer, TournamentBracketSerializer, TournamentPlayerSerializer, TournamentSerializer

# This is a test response
class Test(APIView):
    def get(self, request):
        data = {
            'message': 'Hello, this is a test response!'
        }
        return Response(data)

# Get all matches and create new match
class MatchList(APIView):
    def get(self, request):
        matches = Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get, update, or delete a match
class MatchDetail(APIView):
    def get_object(self, pk):
        try:
            return Match.objects.get(pk=pk)
        except Match.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        match = self.get_object(pk)
        serializer = MatchSerializer(match)
        return Response(serializer.data)
    
    def put(self, request, pk):
        match = self.get_object(pk)
        serializer = MatchSerializer(match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        match = self.get_object(pk)
        match.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Get all players and create new player
class PlayerList(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, update, or delete a player
class PlayerDetail(APIView):
    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        player = self.get_object(pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)
    
    def put(self, request, pk):
        player = self.get_object(pk)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        player = self.get_object(pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Get all players and create new tournament
class TournamentList(APIView):
    def get(self, request):
        tournaments = TournamentList.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, update, or delete a tournament
class TournamentDetail(APIView):
    def get_object(self, pk):
        try:
            return Tournament.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        tournament = self.get_object(pk)
        serializer = TournamentSerializer(tournament)
        return Response(serializer.data)
    
    def put(self, request, pk):
        tournament = self.get_object(pk)
        serializer = TournamentSerializer(tournament, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        tournament = self.get_object(pk)
        tournament.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all player points and create new player point
class PlayerPointList(APIView):
    def get(self, request):
        player_point = Player_Point.objects.all()
        serializer = PlayerPointSerializer(player_point, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PlayerPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, update, or delete a player point
class PlayerPointDetail(APIView):
    def get_object(self, pk):
        try:
            return Player_Point.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        player_point = self.get_object(pk)
        serializer = PlayerPointSerializer(player_point)
        return Response(serializer.data)
    
    def put(self, request, pk):
        player_point = self.get_object(pk)
        serializer = PlayerPointSerializer(player_point, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        player_point = self.get_object(pk)
        player_point.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all player points and create new tournament bracket
class TournamentBracketList(APIView):
    def get(self, request):
        tournament_bracket = Tournament_Bracket.objects.all()
        serializer = TournamentBracketSerializer(tournament_bracket, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TournamentBracketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, update, or delete a tournament brackets
class TournamentBracketDetail(APIView):
    def get_object(self, pk):
        try:
            return Tournament_Bracket.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        tournament_bracket = self.get_object(pk)
        serializer = TournamentBracketSerializer(tournament_bracket)
        return Response(serializer.data)
    
    def put(self, request, pk):
        tournament_bracket = self.get_object(pk)
        serializer = TournamentBracketSerializer(tournament_bracket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        tournament_bracket = self.get_object(pk)
        tournament_bracket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Get all player points and create new tournament players
class TournamentPlayerList(APIView):
    def get(self, request):
        tournament_player = Tournament_Player.objects.all()
        serializer = TournamentPlayerSerializer(tournament_player, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TournamentPlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, update, or delete a tournament players
class TournamentPlayerDetail(APIView):
    def get_object(self, pk):
        try:
            return Tournament_Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        tournament_player = self.get_object(pk)
        serializer = TournamentPlayerSerializer(tournament_player)
        return Response(serializer.data)
    
    def put(self, request, pk):
        tournament_player = self.get_object(pk)
        serializer = TournamentPlayerSerializer(tournament_player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        tournament_player = self.get_object(pk)
        tournament_player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
    


