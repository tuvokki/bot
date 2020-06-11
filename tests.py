import unittest

import requests

from Wernicke import backend


class TestQuestion(unittest.TestCase):
    question = 'What types of beer do you have?'

    def test_pointers(self):
        pointers = backend.get_pointers_from_question(self.question)
        self.assertEqual(pointers, ['beer', 'have'], "Pointers should be 'beer' and 'have'")

    @unittest.skip("This test only works when the backend is running")
    def test_api(self):
        question_data = {'question': self.question}
        resp = requests.get('http://0.0.0.0:8000/api/search',
                            params=question_data)
        reps_data = resp.json()
        self.assertEqual(resp.status_code, 200, 'Is the backend running?')
        self.assertEqual(len(reps_data['answers']), 2)

    if __name__ == '__main__':
        unittest.main()

    def test_synonyms(self):
        word_list = ['time', 'drink', 'healthy']
        synonym_list = backend.get_synonyms_from_words(word_list)
        self.assertIn('time', synonym_list)
        self.assertIn('clock', synonym_list)
        self.assertIn('drink', synonym_list)
        self.assertIn('booze', synonym_list)
        self.assertIn('healthy', synonym_list)
        self.assertIn('goodish', synonym_list)
