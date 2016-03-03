from unittest import TestCase

from practice.string import make_anagram


class Test(TestCase):

    def test1(self):
        assert (True == True)

    def test_make_anagram(self):
        assert make_anagram('aaabbb') == 'YES'
        assert make_anagram('aaabbc') == 'NO'

