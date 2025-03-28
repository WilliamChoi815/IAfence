from django.db import models

class Tournament(models.Model):
    EVENT_TYPE_CHOICES = [
        ("Sabre", "Sabre"),
        ("Foil", "Foil"),
        ("Epee", "Epee"),
    ]
     
    tournament_id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=50, choices = EVENT_TYPE_CHOICES)
    tournament_name = models.CharField(max_length=100)
    tournament_date  = models.DateTimeField()
    completed = models.BooleanField() 
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Match(models.Model):
    MATCH_TYPE_CHOICES = [ 
        ("Group Stage", "Group Stage"),
        ("Round of 256", "Round of 256"),
        ("Round of 128", "Round of 128"),
        ("Round of 64", "Round of 64"),
        ("Round of 32", "Round of 32"),
        ("Round of 16", "Round of 16"),
        ("Quarterfinals", "Quarterfinals"),
        ("Semifinals", "Semifinals"),
        ("Finals", "Finals"),
    ]

    EVENT_TYPE_CHOICES = [
        ("Sabre", "Sabre"),
        ("Foil", "Foil"),
        ("Epee", "Epee"),
    ]

    match_id = models.AutoField(primary_key=True)
    tournament_id = models.ForeignKey("Tournament", on_delete = models.CASCADE, related_name = "tournaments")
    match_type = models.CharField(max_length=50, choices= MATCH_TYPE_CHOICES)
    event_type = models.CharField(max_length=50, choices = EVENT_TYPE_CHOICES)
    match_date = models.DateTimeField()
    player1 = models.ForeignKey("Player", on_delete = models.CASCADE, related_name = "matches_as_player1")
    player1_score = models.IntegerField()
    player2 = models.ForeignKey("Player",on_delete = models.CASCADE, related_name = "matches_as_player2")
    player2_score = models.IntegerField()
    player1_yellowcard = models.IntegerField()
    player2_yellowcard = models.IntegerField()
    player1_forfeit = models.BooleanField()
    player2_forfeit = models.BooleanField()
    completed = models.BooleanField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Player(models.Model):

    EVENT_TYPE_CHOICES = [
        ("Sabre", "Sabre"),
        ("Foil", "Foil"),
        ("Epee", "Epee"),
    ]
     
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=100)
    player_age = models.IntegerField()
    player_affiliation = models.CharField(max_length=100) 
    player_type =  models.CharField(max_length=50, choices = EVENT_TYPE_CHOICES)
    profile_link = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tournament_Bracket(models.Model):
    EVENT_TYPE_CHOICES = [
        ("Sabre", "Sabre"),
        ("Foil", "Foil"),
        ("Epee", "Epee"),
    ]

    tournament_bracket_id = models.AutoField(primary_key=True)
    tournament_id = models.ForeignKey("Tournament", on_delete = models.CASCADE, related_name = "matches")
    event_type = models.CharField(max_length=50, choices = EVENT_TYPE_CHOICES)
    match_id  = models.ForeignKey( "Match", on_delete = models.CASCADE, related_name = "bracket_matches")
    match_number = models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Player_Point(models.Model):
    player_points_id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey("Player", on_delete = models.CASCADE, related_name = "player_points")
    match_id = models.ForeignKey( "Match", on_delete = models.CASCADE, related_name = "point_matches")
    match_date = models.DateTimeField()
    points_earned = models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tournament_Player(models.Model):
    tournament_player_id = models.AutoField(primary_key=True)
    tournament_id = models.ForeignKey("Tournament", on_delete = models.CASCADE, related_name = "player_tournaments")
    player_id = models.ForeignKey("Player", on_delete = models.CASCADE, related_name = "players")
    

    
