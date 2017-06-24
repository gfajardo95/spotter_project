from django.db import models

# Create your models here.


class Workout(models.Model):
    workoutName = models.CharField(max_length=50)
    workoutType = models.CharField(max_length=100)

    def __str__(self):
        return "Workout: {}".format(self.workoutName)


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, related_name="exercises")
    exerciseName = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return "Exercise: {}".format(self.exerciseName)
