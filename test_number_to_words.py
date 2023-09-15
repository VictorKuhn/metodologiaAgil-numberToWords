import unittest
from numbers_to_words import number_to_words

class TestNumberToWords(unittest.TestCase):

    def test_one_digit(self):
        self.assertEqual(number_to_words(5), "five")

    def test_two_digits_hyphenated(self):
        self.assertEqual(number_to_words(21), "twenty-one")

    def test_three_digits(self):
        self.assertEqual(number_to_words(303), "three hundred three")

    def test_four_digits(self):
        self.assertEqual(number_to_words(3466), "three thousand four hundred sixty-six")

if __name__ == '__main__':
    unittest.main()