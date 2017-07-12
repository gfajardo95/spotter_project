from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory

from .api import WorkoutViewSet


# http://127.0.0.1:8000/api/workouts
VALID_TEST_DATA = {
    "id": "1",
    "exercises": [
        {
            "id": "1",
            "exercise_name": "pushups",
            "sets": 5,
            "reps": 5,
            "workout": 1
        }],
    "workout_name": "test",
    "workout_type": "test",
    "created_by": "1"
}


class ApiTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_workout_and_nested_exercises_can_get_POSTed(self):
        # authenticate the request with the root user..
        request = self.factory.post(reverse('api:workout-list'), data=VALID_TEST_DATA, format='json')
        # print(request.body)
        # print(request.get_full_path())

        view = WorkoutViewSet.as_view({'post': 'create'})
        response = view(request)
        # print(response.data)
        # print("\nWorkout's exercises are: ")
        # print(response.data.get('exercises'))
        # print("\nWorkout's workout name is: ")
        # print(response.data.get('workoutName'))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # fix the url
    def test_workout_can_get_deleted(self):
        url = reverse('api:workout-detail', kwargs={'id': 1})
        request = self.factory.delete(path=url, data=VALID_TEST_DATA, format='json')

        view = WorkoutViewSet.as_view({'delete': 'destroy'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_redirects_to_home_page(self):
        pass