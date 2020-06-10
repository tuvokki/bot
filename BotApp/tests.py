import json

from django.test import TestCase
from django.urls import reverse
import backend
from django.test.client import RequestFactory

from BotApp.models import Intent, IntentPointer


class PointerTest(TestCase):
    def setUp(self) -> None:
        i_1 = Intent.objects.create(name='intent1', answer='This is a test.')
        i_2 = Intent.objects.create(name='intent2', answer='This is a tosti.')
        IntentPointer.objects.create(intent=i_1, pointer='test1')
        IntentPointer.objects.create(intent=i_1, pointer='test2')
        IntentPointer.objects.create(intent=i_1, pointer='test3')
        IntentPointer.objects.create(intent=i_2, pointer='tosti1')
        IntentPointer.objects.create(intent=i_2, pointer='tosti2')
        IntentPointer.objects.create(intent=i_2, pointer='tosti3')
        self.factory = RequestFactory()
        self.question = "Is a test1 a thing?"

    def test_get_answer_from_pointer(self):
        pointers = backend.get_pointers_from_question(self.question)
        self.assertIn('test1', pointers)
        intents = list(IntentPointer.objects.filter(pointer__in=pointers).prefetch_related('intent'))
        self.assertEqual(intents[0].intent.answer, 'This is a test.')

    def test_api(self):
        from BotApp.api import ApiAnswer
        api_url = reverse('api-search')
        request = self.factory.get(api_url, data={'question': self.question})
        response = ApiAnswer.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['answers'][0], 'This is a test.')
