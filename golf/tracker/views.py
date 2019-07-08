from django.shortcuts import render
from .models import Season, Match, Player, Course

# Create your views here.
def index(request):
    seasons = Season.objects.all().order_by('-points',)
    matches = Match.objects.all()
    courses = Course.objects.all()
    context = {
        'seasons': seasons,
        'courses': courses,
        'matches': matches
    }
    return render(request, 'tracker/index.html', context)