from django.contrib.auth.models import User

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
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Workout
        fields = '__all__'

    # def create(self, validated_data):
    #     import pdb; pdb.set_trace()
    #     super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    workouts = serializers.PrimaryKeyRelatedField(many=True, queryset=Workout.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'workouts')
