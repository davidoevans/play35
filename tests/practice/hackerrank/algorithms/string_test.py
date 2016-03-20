import pytest
from tests.base import open_to_stdin
from practice.hackerrank.algorithms.string import make_anagram

BASE_DIR = "/Users/davidevans/PycharmProjects/play35/"

def test_make_anagram(capsys):
    in_path = BASE_DIR + "tests/data/practice/hackerrank/algorithms/string/anagram_sample.in"
    out_path = BASE_DIR + "tests/data/practice/hackerrank/algorithms/string/anagram_sample.out"
    with open_to_stdin(in_path):
        n = int(input())
        for i in range(n):
            # print(input())
            print(make_anagram(input()))

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected
