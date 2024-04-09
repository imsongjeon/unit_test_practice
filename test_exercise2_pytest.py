import pytest
from exercise2 import is_valid_email  # Adjust this import based on your project structure

@pytest.mark.parametrize('email,expected', [
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
])
def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected