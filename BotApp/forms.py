from django import forms


class AnswerForm(forms.Form):
    answer = forms.CharField(label='The answer', max_length=250)
    keywords = forms.CharField(label='Keywords', max_length=250)
