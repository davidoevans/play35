import pytest
from tests.base import open_to_stdin
from practice.hackerrank.algorithms.sorting import insertion_sort1
from practice.hackerrank.algorithms.sorting import insertion_sort2

BASE_DIR = "/Users/davidevans/PycharmProjects/play35/"


def test_insertion_sort1(capsys):
    in_path = BASE_DIR + "tests/data/practice/hackerrank/algorithms/sorting/insertion_sort1_sample.in"
    out_path = BASE_DIR + "tests/data/practice/hackerrank/algorithms/sorting/insertion_sort1_sample.out"

    with open_to_stdin(in_path):
        n = int(input().split()[0])
        arr = list(map(int, input().split()))
        insertion_sort1(arr)

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected


def test_insertion_sort2(capsys):
    in_path = BASE_DIR + "tests/data/practice/hackerrank/algorithms/sorting/insertion_sort2_sample.in"
    out_path = BASE_DIR + "tests/data/practice/hackerrank/algorithms/sorting/insertion_sort2_sample.out"

    with open_to_stdin(in_path):
        n = input()
        l = list(map(int, input().split()))
        insertion_sort2(l)

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected
