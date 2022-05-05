from django import forms
from .models import Quiz


class NumsForm(forms.Form):
    questions_num = forms.IntegerField()


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['question_id', 'question', 'answer', 'created_at']
