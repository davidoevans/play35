import pytest
from tests.base import open_to_stdin
from practice.hackerrank.algorithms.sorting import insertion_sort1
from practice.hackerrank.algorithms.sorting import insertion_sort2
from practice.hackerrank.algorithms.sorting import insertion_sort3

BASE_DIR = "/Users/davidevans/PycharmProjects/play35/"


@pytest.mark.parametrize("in_data, out_data", [
    ("tests/data/practice/hackerrank/algorithms/sorting/insertion_sort1_sample.in",
     "tests/data/practice/hackerrank/algorithms/sorting/insertion_sort1_sample.out")
])
def test_insertion_sort1(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data

    with open_to_stdin(in_path):
        n = int(input().split()[0])
        arr = list(map(int, input().split()))
        insertion_sort1(arr)

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected

@pytest.mark.parametrize("in_data, out_data", [
    ("tests/data/practice/hackerrank/algorithms/sorting/insertion_sort2_sample.in",
     "tests/data/practice/hackerrank/algorithms/sorting/insertion_sort2_sample.out")
])
def test_insertion_sort2(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data

    with open_to_stdin(in_path):
        n = input()
        l = list(map(int, input().split()))
        insertion_sort2(l)

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected


@pytest.mark.parametrize("in_data, out_data", [
    ("tests/data/practice/hackerrank/algorithms/sorting/correctness_invariant_sample.in",
     "tests/data/practice/hackerrank/algorithms/sorting/correctness_invariant_sample.out")
])
def test_correctness_invariant(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data
    with open_to_stdin(in_path):
        m = int(input().strip())
        ar = [int(i) for i in input().strip().split()]
        insertion_sort3(ar)
        print(" ".join(map(str, ar)))

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected
