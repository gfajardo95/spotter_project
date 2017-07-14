from django.contrib.auth.models import User
from django.db import models


# it's possible to add a Meta class to these models and set an ordering parameter for example
class Workout(models.Model):
    # uuid = models.UUIDField()
    workout_name = models.CharField(max_length=50)
    workout_type = models.CharField(max_length=100)
    created_by = models.ForeignKey('auth.User', related_name='workouts', on_delete=models.CASCADE)
    # created_date = models.DateField(auto_created=True)

    def __str__(self):
        return "Workout: {}".format(self.workout_name)


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, related_name="exercises")
    exercise_name = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return "Exercise: {}".format(self.exercise_name)
