from django.db import models
from django.utils import timezone

# Create your models here.


class Course(models.Model):
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    par = models.IntegerField()
    slope = models.FloatField( blank=True, null=True)
    
    

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=200)
    handicap = models.CharField(max_length=200, blank=True, null=True)
    @property
    def points(self):
        return 3
        
    

    def __str__(self):
        return self.name

class Match(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    player_one = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_one")
    player_two = models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player_two")
    player_three = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True, related_name="player_three")
    player_four = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True,related_name="player_four")
    player_one_score = models.IntegerField(null=False)
    player_two_score = models.IntegerField(null=False)
    player_three_score = models.IntegerField( blank=True, null=True)
    player_four_score = models.IntegerField( blank=True, null=True)
    played_date = models.DateTimeField(default=timezone.now)
    @property
    def playerCnt(self):
        fields = self._meta.get_fields()
        fields = [x for x in fields if x in ['player_three','player_four']]
        n_count = len([ x for x in fields if getattr(self, x.name) ]) + 2
        return n_count 


    

    def __str__(self):
        return self.player_one.name + " vs " + self.player_two.name