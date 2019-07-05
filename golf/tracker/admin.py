from django.contrib import admin

# Register your models here.
from .models import Player, Course, Match, Season

class SeasonAdmin(admin.ModelAdmin):
    list_display = ('player', 'points', 'wins')

admin.site.register(Player)
admin.site.register(Course)
admin.site.register(Match)
admin.site.register(Season, SeasonAdmin)


