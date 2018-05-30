from django.shortcuts import render
from .models import WorkoutSession

# Create your views here.

def index(request):
    workout_sessions = WorkoutSession.objects.order_by('date_of_workout')
    return render(request, 'index.html', {'workouts': workout_sessions})

def detail(request, workout_session_id):
    return HttpResponse('You are looking at the workout for {}'.format(workout_session_id))

