from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Workout, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
        read_only_fields = ('workout',)


class WorkoutSerializer(WritableNestedModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = '__all__'
