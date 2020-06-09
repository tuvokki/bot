import re

import nltk
from nltk.corpus import wordnet

from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from BotApp.models import Intent, IntentPointer


class IntentListView(ListView):
    context_object_name = 'intent_pointer_list'

    def get_queryset(self):
        return IntentPointer.objects.all().prefetch_related('intent')


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
            print(tokens)
            pos_tagged = nltk.pos_tag(tokens)
            print(f"pos_tagged {pos_tagged}")
            nouns = list(filter(lambda x: x[1] == 'NN', pos_tagged))
            print(f"nouns {nouns}")
            verbs = list(filter(lambda x: x[1] == 'VB', pos_tagged))
            print(f"verbs {verbs}")

            list_syn = {}
            for word in tokens:
                synonyms = []
                for syn in wordnet.synsets(word):
                    for lem in syn.lemmas():
                        # Remove any special characters from synonym strings
                        lem_name = re.sub('[^A-Za-z0-9]+', ' ', lem.name())
                        synonyms.append(lem_name)

                # list_syn[word] = set(synonyms)
                list_syn[word] = synonyms

            # print(list_syn)
            context['list_syn'] = list_syn
            context['nouns'] = nouns
            context['verbs'] = verbs
            intents = list(IntentPointer.objects.filter(pointer__in=[noun[0] for noun in nouns]).prefetch_related('intent'))
            context['intents'] = intents
        return context

    def get(self, request, *args, **kwargs):
        self.question = request.session.get('question', None)
        if self.question:
            del request.session['question']
        return super(SearchView, self).get(request, *args, **kwargs)
