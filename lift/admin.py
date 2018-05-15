from django.contrib import admin

# Register your models here.

from .models import WorkoutSession

admin.site.register(WorkoutSession)
