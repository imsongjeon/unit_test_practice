import unittest
from exercise1 import reverse_string  # Make sure the import path is correct

class TestExercise1(unittest.TestCase):

    def test_reverse_string(self):
        test_cases = [
            ('hello', 'olleh'),
            ('', ''),
            ('hi! How are you?', '?uoy era woH !ih'),
            ('a', 'a'),
            ('123456', '654321'),
            ('racecar', 'racecar'),
            ('Python Programming', 'gnimmargorP nohtyP'),
            (' spaces ', ' secaps '),
            ('CAPITAL', 'LATIPAC'),
            ('2023@AI', 'IA@3202')
        ]

        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                self.assertEqual(reverse_string(input), expected)

if __name__ == '__main__':
    unittest.main()
