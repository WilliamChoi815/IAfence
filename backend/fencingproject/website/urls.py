from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.Test.as_view(), name = "test"),
    path('matches/', views.MatchList.as_view(), name = "match-list"),
    path('matches/<int:pk>/', views.MatchDetail.as_view(), name = "match-detail"),
    path('tournaments/', views.TournamentList.as_view(), name = "tournament-list"),
    path('tournaments/<int:pk>/', views.TournamentDetail.as_view(), name = "tournament-detail"),
    path('players/', views.PlayerList.as_view(), name = "players-list"),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name = "player-detail"),
    path('players_points/', views.PlayerPointList.as_view(), name = "players-points-list"),
    path('players_points/<int:pk>/', views.PlayerPointDetail.as_view(), name = "player-points-detail"),
    path('tournament_brackets/', views.TournamentBracketList.as_view(), name = "tournament-bracket-list"),
    path('tournament_brackets/<int:pk>/', views.TournamentBracketDetail.as_view(), name = "tournament-bracket-detail"),
    path('tournament_players/', views.TournamentPlayerList.as_view(), name = "tournament-player-list"),
    path('tournament_players/<int:pk>/', views.TournamentPlayerDetail.as_view(), name = "tournament-player-detail"),
]