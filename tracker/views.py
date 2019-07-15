from django.shortcuts import render
from django.views.generic.detail import DetailView
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

class MatchDetailView(DetailView):
    
    model = Match
    template_name = "tracker/match.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SeasonDetailView(DetailView):
    
    model = Season
    template_name = "tracker/season.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CourseDetailView(DetailView):
    
    model = Course
    template_name = "tracker/course.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context