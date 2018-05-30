from django.db import models
import uuid


class WorkoutSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_workout = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

class LiftEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    LIFTS = (
        ('BP', 'Bench Press'),
        ('SQ', 'Squat'),
        ('OHP', 'Overhead Press'),
        ('DL', 'Deadlift')
    )

    RPE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('7.5', '7.5'),
        ('8', '8'),
        ('8.5', '8.5'),
        ('9', '9'),
        ('9.5', '9.5'),
        ('10', '10'),
    )

    lift_type = models.CharField(max_length=3, choices=LIFTS)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()
    rpe = models.CharField(max_length=3, choices=RPE)
    notes = models.TextField()

    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)
