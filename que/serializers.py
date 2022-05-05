from rest_framework import serializers
from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['id', 'question_id', 'question', 'answer', 'created_at']
