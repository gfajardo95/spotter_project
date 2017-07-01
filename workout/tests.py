from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory

from .api import WorkoutViewSet

# Create your tests here
# http://127.0.0.1:8000/api/workouts/
VALID_TEST_DATA = {
    "id": 1,
    "exercises": [
        {
            "id": 1,
            "exerciseName": "pushups",
            "sets": 5,
            "reps": 5,
            "workout": 1
        }],
    "workoutName": "test",
    "workoutType": "test"
}


class ApiTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    # I currently get a 500 so I hope to replicate this here, and
    # see where I'm messing up in the implementation
    def test_workout_can_get_POSTed(self):
        request = self.factory.post(reverse('api:workout-list'), data=VALID_TEST_DATA, format='json')
        print(request.body)
        print(request.get_full_path())
        view = WorkoutViewSet.as_view({'POST': 'create'})

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
