from lift.models import WorkoutSession
from unittest import TestCase


class TestModels(TestCase):

    def setUp(self):
        WorkoutSession.objects.all().delete()
        self.workout_session = WorkoutSession(notes='good lift today').save()

    @pytest.mark.django_db
    def test_has_some_entries(self):
        pass

