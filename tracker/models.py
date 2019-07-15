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
    hometown = models.CharField(max_length=200, blank=True, null=True)
    handicap = models.CharField(max_length=200, blank=True, null=True)
    pic_url = models.URLField(max_length=250, blank=True, null=True)

    


    def __str__(self):
        return self.name

class Season(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    points = models.IntegerField( blank=True, null=True, default=0)
    wins = models.IntegerField( blank=True, null=True, default=0)

    def __str__(self):
        return self.player.name

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
    ranked = models.BooleanField(blank=True, null=True)
    points = models.IntegerField( blank=True, null=True)
    @property
    def playerCnt(self):
        cnt = 2
        if self.player_three:
            cnt +=1
        if self.player_four:
            cnt+=1
        return cnt 
    def getResults(self):
        
        cnt = self.playerCnt
        print("p cnt is "+ str(cnt))
        scores = [(self.player_one, self.player_one_score),
                    (self.player_two, self.player_two_score),
                    (self.player_three, self.player_three_score),
                    (self.player_four, self.player_four_score)
            ]
        scores = scores[0:cnt]
        scores.sort(key=lambda tup: tup[1])
        
        ranks = {}
        for i , score in enumerate(scores):
            if i + 1 == 1:
                dif = 0
            else:
                dif = i + 1
            ranks[score[0]] = (i + 1, self.points - dif )   
        return ranks
    
    def save(self, *args, **kwargs):
    
        results = self.getResults()
        print(results)
        for key, value in results.items():
            stat = Season.objects.filter(player=key)[0]
            print(stat)
            stat.points = stat.points + value[1]
            if value[0] == 1:
                stat.wins += 1
            stat.save()
            # Object is a new instance

        return super(Match, self).save(*args, **kwargs)     
            

    


    

    def __str__(self):
        return self.player_one.name + " vs " + self.player_two.name