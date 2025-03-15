from django.db import models

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
    #tournament_id = models.ForeignKey("Tournament", on_delete = models.CASCADE, related_name = "matches")
    match_type = models.CharField(max_length=50, choices= MATCH_TYPE_CHOICES)
    event_type = models.CharField(max_length=50, choices = EVENT_TYPE_CHOICES)
    match_date = models.DateTimeField()
    #player1 = models.ForeignKey("Player", related_name = "matches_as_player1")
    player1_score = models.IntegerField()
    #player2 = models.ForeignKey("Player", related_name = "matches_as_player2")
    player2_score = models.IntegerField()
    player1_yellowcard = models.IntegerField()
    player2_yellowcard = models.IntegerField()
    player1_forfeit = models.BooleanField()
    player2_forfeit = models.BooleanField()
    completed = models.BooleanField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
