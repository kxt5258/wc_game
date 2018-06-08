from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=3)

    def __str__(self):
        return self.country_name


class Player(models.Model):
    player_name = models.CharField(max_length=200)
    team_one = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_one")
    team_two = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_two")
    team_three = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_three")
    team_four = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_four")

    def __str__(self):
        return self.player_name


class Team(models.Model):
    team = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="team")
    goal = models.IntegerField(blank=True, null=True)
    concede = models.IntegerField(blank=True, null=True, default=0)
    gd = models.IntegerField(blank=True, null=True, default=0)
    point = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    match_order = models.TextField(max_length=6, blank=True, null=True, unique=True)

    def __str__(self):
        return self.match_order

    def save(self, *args, **kwargs):
        self.gd = int(self.goal) - int(self.concede)
        if self.goal > self.concede:
            self.win = 1
            self.point = 3
        elif self.goal < self.concede:
            self.loss = 1
            self.point = 0
        else:
            self.draw = 1
            self.point = 1
        super(Team, self).save(*args, **kwargs)


class Match(models.Model):
    match_order = models.IntegerField()
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_one", blank=True, null=True)
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_two", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
