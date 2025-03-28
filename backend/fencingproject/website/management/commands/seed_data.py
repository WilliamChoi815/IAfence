# myapp/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from datetime import timedelta

from website.models import (
    Tournament,
    Match,
    Player,
    Tournament_Bracket,
    Player_Point,
    Tournament_Player,
)

class Command(BaseCommand):
    help = "Seed the database with realistic data for Tournaments, Matches, Players, Brackets, and Points."

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")

        # 1. (OPTIONAL) Clear existing data. Useful in development to start fresh.
        #    Comment out or remove in production!
        Player_Point.objects.all().delete()
        Tournament_Bracket.objects.all().delete()
        Match.objects.all().delete()
        Tournament_Player.objects.all().delete()
        Player.objects.all().delete()
        Tournament.objects.all().delete()

        # Possible weapon/event types
        event_types = ["Sabre", "Foil", "Epee"]

        # For a single-elimination bracket of 8 players, we have:
        # Quarterfinals: match_numbers 1..4
        # Semifinals: match_numbers 5..6
        # Final: match_number 7
        bracket_names = {
            1: "Quarterfinals",
            2: "Quarterfinals",
            3: "Quarterfinals",
            4: "Quarterfinals",
            5: "Semifinals",
            6: "Semifinals",
            7: "Final",
        }

        # 2. Create 2 Tournaments,
        #    each with a random event_type (Sabre, Foil, Epee).
        for i in range(2):
            t_type = random.choice(event_types)
            tournament_obj = Tournament.objects.create(
                event_type=t_type,
                tournament_name=f"Sample {t_type} Tournament {i+1}",
                tournament_date=timezone.now() + timedelta(days=10 * (i + 1)),
                completed=False
            )

            # 3. Create 8 Players for this tournament,
            #    each with the SAME player_type as the tournament.
            tournament_players = []
            for j in range(8):
                player_obj = Player.objects.create(
                    player_name=f"{t_type} Player {i+1}-{j+1}",
                    player_age=random.randint(18, 40),
                    player_affiliation=f"FencingClub{random.randint(1,5)}",
                    player_type=t_type,
                    profile_link="https://example.com/player-profile"
                )
                tournament_players.append(player_obj)

                # Link player to the tournament via Tournament_Player
                Tournament_Player.objects.create(
                    tournament_id=tournament_obj,
                    player_id=player_obj
                )

            # 4. Create Matches for a single-elimination bracket
            matches = []
            for match_num in range(1, 8):
                # For seeding/demo, just pick any 2 from tournament_players
                # In a real bracket system, you’d carefully pick winners from previous matches.
                player1, player2 = random.sample(tournament_players, 2)

                match_obj = Match.objects.create(
                    tournament_id=tournament_obj,
                    match_type=bracket_names[match_num],
                    event_type=t_type,
                    match_date=timezone.now() + timedelta(days=random.randint(1, 5)),
                    player1=player1,
                    player1_score=random.randint(5, 15),
                    player2=player2,
                    player2_score=random.randint(5, 15),
                    player1_yellowcard=random.randint(0, 2),
                    player2_yellowcard=random.randint(0, 2),
                    player1_forfeit=False,
                    player2_forfeit=False,
                    completed=True  # For demo: mark them completed
                )
                matches.append(match_obj)

                # Create the bracket record
                Tournament_Bracket.objects.create(
                    tournament_id=tournament_obj,
                    event_type=t_type,
                    match_id=match_obj,
                    match_number=match_num
                )

            # 5. Create Player_Points for each match
            for m in matches:
                Player_Point.objects.create(
                    player_id=m.player1,
                    match_id=m,
                    match_date=m.match_date,
                    points_earned=m.player1_score
                )
                Player_Point.objects.create(
                    player_id=m.player2,
                    match_id=m,
                    match_date=m.match_date,
                    points_earned=m.player2_score
                )

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))