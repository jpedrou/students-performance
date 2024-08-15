from django.db import models


class PredictionResults(models.Model):
        sex = models.CharField(max_length=10)
        race = models.CharField(max_length=50)
        parental_level_of_education = models.CharField(max_length=100)
        lunch = models.CharField(max_length=10)
        test_preparation_course = models.CharField(max_length=10)
        reading_score = models.IntegerField()
        writing_score = models.IntegerField()
        math_score_predicton = models.IntegerField()
