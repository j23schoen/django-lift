from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkoutSession

# Create your views here.

def index(request):
    workout_sessions = WorkoutSession.objects.order_by('date_of_workout')
    output = ', '.join([ws.notes for ws in workout_sessions])
    return HttpResponse(output)

def detail(request, workout_session_id):
    return HttpResponse('You are looking at the workout for {}'.format(workout_session_id))