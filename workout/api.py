from rest_framework.viewsets import ModelViewSet

from .models import Workout, Exercise
from .serializers import WorkoutSerializer, ExerciseSerializer


class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout = Workout.objects.create(**validated_data)

        for exercise_data in exercises_data:
            Exercise.objects.create(workout=workout, **exercise_data)

        return workout


class ExerciseViewSet(ModelViewSet):
    print('in the ExerciseViewSet')
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
