import pytest
from tests.base import open_to_stdin
from practice.hackerrank.algorithms.sorting import insertion_sort1
from practice.hackerrank.algorithms.sorting import insertion_sort2
from practice.hackerrank.algorithms.sorting import insertion_sort3
from practice.hackerrank.algorithms.sorting import running_time
from practice.hackerrank.algorithms.sorting import counting_sort3
from practice.hackerrank.algorithms.sorting import quick_sort1
from practice.hackerrank.algorithms.sorting import quick_sort2
from practice.hackerrank.algorithms.sorting import quick_sort3

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


@pytest.mark.parametrize("in_data, out_data", [
    ("tests/data/practice/hackerrank/algorithms/sorting/running_time_sample.in",
     "tests/data/practice/hackerrank/algorithms/sorting/running_time_sample.out")
])
def test_running_time(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data
    with open_to_stdin(in_path):
        m = int(input().strip())
        ar = [int(i) for i in input().strip().split()]
        print(running_time(ar))

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected


@pytest.mark.parametrize("in_data, out_data", [
    ("tests/data/practice/hackerrank/algorithms/sorting/counting_sort3_sample.in",
     "tests/data/practice/hackerrank/algorithms/sorting/counting_sort3_sample.out")
])
def test_counting_sort3(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data
    with open_to_stdin(in_path):
        m = int(input().strip())
        ar = [int(input().strip().split()[0]) for x in range(m)]
        print(" ".join(repr(e) for e in list(counting_sort3(ar))))

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected


@pytest.mark.parametrize("in_data, out_data", [
    ("tests/data/practice/hackerrank/algorithms/sorting/quick_sort1_sample.in",
     "tests/data/practice/hackerrank/algorithms/sorting/quick_sort1_sample.out")
])
def test_quick_sort1(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data
    with open_to_stdin(in_path):
        m = int(input().strip())
        ar = [int(i) for i in input().strip().split()]
        print(quick_sort1(ar))

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected

@pytest.mark.parametrize("in_data, out_data", [
    ("tests/data/practice/hackerrank/algorithms/sorting/quick_sort2_sample.in",
     "tests/data/practice/hackerrank/algorithms/sorting/quick_sort2_sample.out")
])
def test_quick_sort2(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data
    with open_to_stdin(in_path):
        m = int(input().strip())
        ar = [int(i) for i in input().strip().split()]
        print(" ".join(repr(x) for x in quick_sort2(ar)))

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected

@pytest.mark.parametrize("in_data, out_data", [
    ("tests/data/practice/hackerrank/algorithms/sorting/quick_sort3_sample.in",
     "tests/data/practice/hackerrank/algorithms/sorting/quick_sort3_sample.out")
])
def test_quick_sort3(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data
    with open_to_stdin(in_path):
        m = int(input().strip())
        ar = [int(i) for i in input().strip().split()]
        quick_sort3(ar, 0, len(ar)-1)

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected
