from django.contrib import admin

from .models import Character, Movie, Phase, Platform

# Register your models here.

admin.site.register(Character)
admin.site.register(Movie)
admin.site.register(Phase)
admin.site.register(Platform)