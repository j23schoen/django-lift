from django.contrib import admin

# Register your models here.

from .models import WorkoutSession, LiftEntry

admin.site.register(WorkoutSession)
admin.site.register(LiftEntry)
