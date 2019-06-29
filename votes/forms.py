# votes/forms.py
from django import forms

from .models import VoteResponse, VoteQuestion


# class VoteForm(forms.ModelForm):
#     class Meta:
#         model = VoteResponse
#         fields = ('v_response', )


class VoteQuestionForm(forms.ModelForm):
    class Meta:
        model = VoteQuestion
        fields = ('title', 'prompt', 'contents', 'is_active', 'code', )
