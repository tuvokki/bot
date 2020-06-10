from json_views.views import JSONDataView

import backend
from BotApp.models import IntentPointer


class ApiAnswer(JSONDataView):
    question = None
    intents = None

    def get_context_data(self, **kwargs):
        context = super(ApiAnswer, self).get_context_data(**kwargs)
        if 'question' in self.request.GET:
            self.question = self.request.GET['question']
            pointers = backend.get_pointers_from_question(self.question)
            self.intents = list(IntentPointer.objects.filter(pointer__in=pointers).prefetch_related('intent'))
            context['answers'] = []
            for intent in self.intents:
                context['answers'].append(intent.intent.answer)
        return context
