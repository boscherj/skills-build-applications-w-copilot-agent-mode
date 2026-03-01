from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User(username='spiderman', email='spiderman@marvel.com', password='test123')
        self.assertEqual(user.username, 'spiderman')


class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team(name='Team Marvel', members=[])
        self.assertEqual(team.name, 'Team Marvel')


class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity(user='spiderman', activity_type='running', duration=30.0, date='2024-01-01')
        self.assertEqual(activity.activity_type, 'running')


class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        entry = Leaderboard(user='spiderman', score=100.0)
        self.assertEqual(entry.score, 100.0)


class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout(name='Hero Training', description='Train like a superhero', duration=60.0)
        self.assertEqual(workout.name, 'Hero Training')
