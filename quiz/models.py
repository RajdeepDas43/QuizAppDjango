from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # A, B, C, or D

    def __str__(self):
        return self.text

class UserQuizSession(models.Model):
    total_attempts = models.IntegerField(default=0)
    correct_attempts = models.IntegerField(default=0)
    incorrect_attempts = models.IntegerField(default=0)

    def __str__(self):
        return f"Session: {self.total_attempts} attempts"
