from django.shortcuts import render
from django.http import Http404
from django.utils import timezone
from django.db.models import Sum
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
        tournaments = Tournament.objects.all()
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
""" 
Actual API views used currently
"""
class PlayerRankingView(APIView):
    def get(self, request, category, format=None):
        current_year = timezone.now().year
        top = request.GET.get('top', None) 
        yearly_rankings = (
            Player_Point.objects
            .filter(
                player_id__player_type=category,
                match_date__year=current_year
            )
            .values(
                'player_id',
                'player_id__player_name',
                'player_id__player_age',
                'player_id__player_affiliation'
            )
            .annotate(total_points=Sum('points_earned'))
            .order_by('-total_points')
        )
        if top and top.isdigit():
            top_limit = int(top)
            yearly_rankings = yearly_rankings[:top_limit]
        data = []
        for idx, record in enumerate(yearly_rankings, start=1):
            data.append({
                "rank": idx,
                "player_name": record["player_id__player_name"],
                "age": record["player_id__player_age"],
                "affiliation": record["player_id__player_affiliation"],
                "total_points": record["total_points"] or 0,
            })

        return Response(data)
    

class RecentMatchesView(APIView):
    def get(self, request, category, format=None):
        recent_matches = (
            Match.objects
            .select_related('tournament_id', 'player1', 'player2')
            .filter(event_type=category)        
            .order_by('-match_date')[:5]
        )

        data = []
        for match in recent_matches:
            p1_name = match.player1.player_name
            p1_affiliation = match.player1.player_affiliation
            p1_score = match.player1_score
            p1_yellow = match.player1_yellowcard

            if p1_yellow == 0:
                p1_yellow_count = 0
                p1_red_count = 0
            elif p1_yellow == 1:
                p1_yellow_count = 1
                p1_red_count = 0
            else:  
                p1_yellow_count = 1
                p1_red_count = p1_yellow - 1

            p2_name = match.player2.player_name
            p2_affiliation = match.player2.player_affiliation
            p2_score = match.player2_score
            p2_yellow = match.player2_yellowcard

            if p2_yellow == 0:
                p2_yellow_count = 0
                p2_red_count = 0
            elif p2_yellow == 1:
                p2_yellow_count = 1
                p2_red_count = 0
            else:
                p2_yellow_count = 1
                p2_red_count = p2_yellow - 1

            data.append({
                "tournament_name": match.tournament_id.tournament_name,
                "tournament_date": match.tournament_id.tournament_date.date(),
                "round": match.match_type,

                # Player1 info
                "player_1_name": p1_name,
                "player_1_affiliation": p1_affiliation,
                "player_1_score": p1_score,
                "player_1_yellow_card_count": p1_yellow_count,
                "player_1_red_card_count": p1_red_count,

                # Player2 info
                "player_2_name": p2_name,
                "player_2_affiliation": p2_affiliation,
                "player_2_score": p2_score,
                "player_2_yellow_card_count": p2_yellow_count,
                "player_2_red_card_count": p2_red_count,
            })

        return Response(data)