import unittest

import requests

import backend


class TestQuestion(unittest.TestCase):
    question = 'What types of beer do you have?'

    def test_pointers(self):
        pointers = backend.get_pointers_from_question(self.question)
        self.assertEqual(pointers, ['beer', 'have'], "Pointers should be 'beer' and 'have'")

    def test_api(self):
        question_data = {'question': self.question}
        resp = requests.get('http://0.0.0.0:8000/api/search',
                            params=question_data)
        reps_data = resp.json()
        self.assertEqual(resp.status_code, 200, 'Is the backend running?')
        self.assertEqual(len(reps_data['answers']), 2)

    if __name__ == '__main__':
        unittest.main()
