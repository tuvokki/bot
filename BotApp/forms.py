from django import forms

from BotApp.models import Intent


class AnswerForm(forms.Form):
    answer = forms.CharField(label='The answer', max_length=250)
    keywords = forms.CharField(label='Keywords', max_length=250)
    intent = forms.ModelChoiceField(queryset=Intent.objects.all().order_by('name'), required=False)
