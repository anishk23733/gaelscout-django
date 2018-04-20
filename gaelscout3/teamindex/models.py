from django.db import models

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=10,
                            blank=False,
                            unique=True)
    avg_opr = models.DecimalField(max_digits=5,
                                decimal_places=2)
    avg_mscore = models.DecimalField(max_digits=5,
                                decimal_places=2)
    opr_percentile = models.DecimalField(max_digits=5,
                                decimal_places=2)
    mscore_percentile = models.DecimalField(max_digits=5,
                                decimal_places=2)

class ResearchTeams(models.Model):
    name = models.CharField(max_length=10,blank=False,unique=True)
    opr = models.DecimalField(max_digits=5,
                                decimal_places=2)
    mscore = models.DecimalField(max_digits=5,
                                decimal_places=2)
    rank = models.DecimalField(max_digits=5,
                                decimal_places=2)
    opr_percentile = models.DecimalField(max_digits=5,
                                decimal_places=2)
    mscore_percentile = models.DecimalField(max_digits=5,
                                decimal_places=2)
    w = models.IntegerField()
    l = models.IntegerField()
class Matches(models.Model):
    number = models.CharField(max_length=10,blank=False)
    field = models.CharField(max_length=10,blank=False)
    day = models.CharField(max_length=10,blank=False)
    time = models.CharField(max_length=10,blank=False)
    phase = models.CharField(max_length=10,blank=False)
    
    red1 = models.CharField(max_length=10,blank=False)
    red1_opr = models.DecimalField(max_digits=5,
                                decimal_places=2)
    red1_mscore = models.DecimalField(max_digits=5,
                                decimal_places=2)
    red2 = models.CharField(max_length=10,blank=False)

    red2_opr = models.DecimalField(max_digits=5,
                                decimal_places=2)
    red2_mscore = models.DecimalField(max_digits=5,
                                decimal_places=2)
    blue1 = models.CharField(max_length=10,blank=False)
    blue1_opr = models.DecimalField(max_digits=5,
                                decimal_places=2)
    blue1_mscore = models.DecimalField(max_digits=5,
                                decimal_places=2)
    blue2 = models.CharField(max_length=10,blank=False)
    blue2_opr = models.DecimalField(max_digits=5,
                                decimal_places=2)
    blue2_mscore = models.DecimalField(max_digits=5,
                                decimal_places=2)
    winner = models.CharField(max_length=1,blank=False)
    chance = models.DecimalField(max_digits=5,
                                decimal_places=2)
