from django.db import models


class Quiz(models.Model):
    question_id = models.IntegerField(blank=False)
    question = models.TextField(blank=False)
    answer = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=False)
