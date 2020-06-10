from django.test import TestCase
import backend

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

    def test_get_answer_from_pointer(self):
        question = "Is a test1 a thing?"
        pointers = backend.get_pointers_from_question(question)
        self.assertIn('test1', pointers)
        intents = list(IntentPointer.objects.filter(pointer__in=pointers).prefetch_related('intent'))
        self.assertEqual(intents[0].intent.answer, 'This is a test.')