from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

from .models import Workout, Exercise
from .serializers import WorkoutSerializer, ExerciseSerializer, UserSerializer


class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()
        serializer.save(created_by=self.request.user)


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
