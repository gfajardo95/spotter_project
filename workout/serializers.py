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
    password = serializers.HiddenField(default='')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'workouts', 'password')

    # password isn't set when it's created.. this gives an error
    # def create(self, validated_data):
    #     validated_data['password'] = self.context['request'].data['password']
    #     user = User.objects.create(**validated_data)
    #     return user


class WorkoutSerializer(WritableNestedModelSerializer):
    exercises = ExerciseSerializer(many=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Workout
        fields = ('id', 'created_by', 'workout_name', 'workout_type', 'exercises')

    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance
