from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matches/<int:pk>/', views.MatchDetailView.as_view(), name='match'),
    path('player/<int:pk>/', views.SeasonDetailView.as_view(), name='season'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course')
 
]