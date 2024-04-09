import unittest
from exercise2 import is_valid_email  # Adjust this import based on your project structure

class TestExercise2(unittest.TestCase):
    def test_is_valid_email(self):
        test_cases = [
            ('example@example.com', True),
            ('plainaddress', False),
            ('john.doe@com', False),
            ('@example.com', False),
            ('jane.doe@example', False),
            ('user@localhost', True),  
            ('user.name+tag@domain.com', True),
            ('user!#$%&\'*+/=?^_`{|}~-@domain.com', True),
            ('user@domain..com', False),
            ('user@-domain.com', False)
        ]

        for email, expected in test_cases:
            with self.subTest(email=email, expected=expected):
                self.assertEqual(is_valid_email(email), expected)

if __name__ == '__main__':
    unittest.main()
