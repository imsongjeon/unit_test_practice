import pytest

from exercise1 import reverse_string

@pytest.mark.parametrize('input,expected', [
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
])
def test_reverse_string(input, expected):
    assert reverse_string(input) == expected