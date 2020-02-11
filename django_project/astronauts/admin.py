from django.contrib import admin

from astronauts.models import Astronaut


@admin.register(Astronaut)
class AstronautAdmin(admin.ModelAdmin):
    pass