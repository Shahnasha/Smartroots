from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    SKILL_CHOICES = [
        ('speaking', 'Speaking'),
        ('listening', 'Listening'),
        ('reading', 'Reading'),
        ('writing', 'Writing'),
        ('drawing', 'Drawing'),
        ('moving', 'Moving'),
        ('playing with others', 'Playing with Others'),
    ]

    ENVIRONMENT_CHOICES = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
        ('flexible', 'Flexible'),
    ]

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=SKILL_CHOICES)
    level = models.IntegerField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    environment = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} completed {self.activity.title}"
    

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True)  # Optional 1–5 stars

    def __str__(self):
        return f"Feedback from {self.user.username} at {self.submitted_at}"

