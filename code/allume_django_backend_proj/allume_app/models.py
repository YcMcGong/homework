from django.db import models
# django time zone
from django.utils import timezone

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length = 100, primary_key = True, unique = True)
    answer = models.CharField(max_length = 250)
    datetime = models.DateTimeField(default=timezone.now) # datetime to sort questions if needed

class Testimonial(models.Model):
    styling_goal = models.CharField(max_length = 100, primary_key = True, unique = True)
    testimonial = models.CharField(max_length = 500)
    datetime = models.DateTimeField(default=timezone.now) # datetime to sort questions if needed