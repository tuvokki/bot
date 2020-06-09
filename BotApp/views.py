import logging

import nltk

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, CreateView, FormView
from BotApp.models import IntentPointer, Intent
from BotApp.forms import AnswerForm

logger = logging.getLogger(__name__)


class IntentListView(ListView):
    context_object_name = 'intent_list'
    template_name = 'BotApp/intent_list.html'

    def get_queryset(self):
        return Intent.objects.all()


class SearchView(TemplateView):
    template_name = 'BotApp/search.html'
    question = None

    def post(self, request, *args, **kwargs):
        request.session['question'] = request.POST['question']
        return HttpResponseRedirect(reverse('search'))

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data()
        if self.question:
            context['question'] = self.question
            tokens = nltk.word_tokenize(text=self.question)
            pos_tagged = nltk.pos_tag(tokens)
            logger.debug(f"pos_tagged {pos_tagged}")
            nouns = list(filter(lambda x: x[1] == 'NN', pos_tagged))
            logger.debug(f"nouns {nouns}")
            verbs = list(filter(lambda x: x[1] == 'VB', pos_tagged))
            logger.debug(f"verbs {verbs}")

            pointers = [noun[0] for noun in nouns] + [verb[0] for verb in verbs]
            intents = list(IntentPointer.objects.filter(pointer__in=pointers).prefetch_related('intent'))
            context['pointers'] = pointers
            context['intents'] = intents
        return context

    def get(self, request, *args, **kwargs):
        self.question = request.session.get('question', None)
        if self.question:
            del request.session['question']
        return super(SearchView, self).get(request, *args, **kwargs)


class NewAnswerView(FormView):
    template_name = 'BotApp/new_answer.html'
    form_class = AnswerForm
    success_url = '/list/'

    def form_valid(self, form):
        if not form.cleaned_data['intent']:
            a_name = form.cleaned_data['keywords'].replace(', ', '')
            intent = Intent.objects.create(name=a_name, answer=form.cleaned_data['answer'])
        else:
            intent = Intent.objects.get(name=form.cleaned_data['intent'])

        for pointer in form.cleaned_data['keywords'].replace(',','').split():
            IntentPointer.objects.create(intent=intent, pointer=pointer)
        return super(NewAnswerView, self).form_valid(form)