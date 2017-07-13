from django.contrib.auth.models import User

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Workout, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
        read_only_fields = ('workout',)


class UserSerializer(serializers.ModelSerializer):
    workouts = serializers.PrimaryKeyRelatedField(many=True, queryset=Workout.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'workouts')


class WorkoutSerializer(WritableNestedModelSerializer):
    exercises = ExerciseSerializer(many=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Workout
        fields = ('id', 'created_by', 'workout_name', 'workout_type', 'exercises')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        instance = super().create(validated_data)
        return instance
