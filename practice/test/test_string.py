import pytest
from unittest import TestCase

from practice.string import make_anagram


@pytest.fixture()
def anagram_data():
    return 'hi'


def test1(anagram_data):
    assert anagram_data == 'hi'


def test_make_anagram():
    assert make_anagram('aaabbb') == 3
    assert make_anagram('aaabbc') == 3

