from django.db import models

# Create your models here.
class Goal(models.Model):
    goal_name = models.CharField(max_length=(255))
    goal_description = models.CharField(max_length=(255), null=True)
    goal_start = models.DateField(null = True)
    goal_end = models.DateField(null = True)