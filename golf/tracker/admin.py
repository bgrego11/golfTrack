from django.contrib import admin

# Register your models here.
from .models import Player, Course, Match

admin.site.register(Player)
admin.site.register(Course)
admin.site.register(Match)