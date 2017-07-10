from django import forms

from . import models

class QuizForm(forms.ModelForm):        #we are using forms.ModelForm instead pof forms.Form
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions',
        ]

class TrueFalseQuestionForm(forms.ModelForm):
    class Meta:
        models = models.TrueFalseQuestion
        fields = ['order', 'prompt']

class MultipleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = ['order', 'prompt', 'shuffle_answers']
        

