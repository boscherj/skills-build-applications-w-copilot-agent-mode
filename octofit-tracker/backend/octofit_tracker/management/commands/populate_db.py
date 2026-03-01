from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users (superheroes)
        users = [
            User(username='spiderman', email='spiderman@marvel.com', password=make_password('webslinger123')),
            User(username='ironman', email='ironman@marvel.com', password=make_password('jarvis123')),
            User(username='batman', email='batman@dc.com', password=make_password('darknight123')),
            User(username='superman', email='superman@dc.com', password=make_password('krypton123')),
            User(username='thor', email='thor@marvel.com', password=make_password('mjolnir123')),
        ]
        for user in users:
            user.save()
        self.stdout.write(self.style.SUCCESS(f'Created {len(users)} users'))

        # Create teams
        team_marvel = Team(
            name='Team Marvel',
            members=['spiderman', 'ironman', 'thor']
        )
        team_marvel.save()

        team_dc = Team(
            name='Team DC',
            members=['batman', 'superman']
        )
        team_dc.save()
        self.stdout.write(self.style.SUCCESS('Created 2 teams'))

        # Create activities
        activities = [
            Activity(user='spiderman', activity_type='running', duration=30.0, date=date(2024, 1, 10)),
            Activity(user='ironman', activity_type='strength training', duration=45.0, date=date(2024, 1, 11)),
            Activity(user='batman', activity_type='martial arts', duration=60.0, date=date(2024, 1, 12)),
            Activity(user='superman', activity_type='flying', duration=20.0, date=date(2024, 1, 13)),
            Activity(user='thor', activity_type='hammer throwing', duration=30.0, date=date(2024, 1, 14)),
        ]
        for activity in activities:
            activity.save()
        self.stdout.write(self.style.SUCCESS(f'Created {len(activities)} activities'))

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user='batman', score=300.0),
            Leaderboard(user='ironman', score=275.0),
            Leaderboard(user='thor', score=250.0),
            Leaderboard(user='spiderman', score=225.0),
            Leaderboard(user='superman', score=200.0),
        ]
        for entry in leaderboard_entries:
            entry.save()
        self.stdout.write(self.style.SUCCESS(f'Created {len(leaderboard_entries)} leaderboard entries'))

        # Create workouts
        workouts = [
            Workout(
                name='Hero Cardio',
                description='High-intensity cardio workout for superheroes',
                duration=30.0
            ),
            Workout(
                name='Strength of Steel',
                description='Build super strength with these exercises',
                duration=45.0
            ),
            Workout(
                name='Agility Training',
                description='Improve agility and reflexes like a superhero',
                duration=40.0
            ),
            Workout(
                name='Endurance Challenge',
                description='Build endurance to fight crime all night long',
                duration=60.0
            ),
            Workout(
                name='Speed Boost',
                description='Run faster than a speeding bullet',
                duration=25.0
            ),
        ]
        for workout in workouts:
            workout.save()
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workouts'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data'))
