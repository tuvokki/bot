import unittest
import backend


class TestQuestion(unittest.TestCase):

    def test_pointers(self):
        question = "What types of beer do you have?"
        pointers = backend.get_pointers_from_question(question)
        self.assertEqual(pointers, ['beer', 'have'], "Pointers should be 'beer' and 'have'")


if __name__ == '__main__':
    unittest.main()
