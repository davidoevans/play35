import pytest
from tests.base import open_to_stdin
# from tests.base import pytest_generate_tests
from practice.hackerrank.algorithms.dynamic_programming import fib_modified

BASE_DIR = "/Users/davidevans/PycharmProjects/play35/"

scenario1 = ('sample', {'test_name': 'grid_search', 'test_id': 'sample'})
scenario7 = ('7', {'test_name': 'grid_search', 'test_id': '7'})

def test_fibonacci_modified(capsys):

    scenarios = [scenario1, scenario7]

    in_path = BASE_DIR + "tests/data/practice/hackerrank/algorithms/dynamic_programming/fibonacci_modified_sample.in"
    out_path = BASE_DIR + "tests/data/practice/hackerrank/algorithms/dynamic_programming/fibonacci_modified_sample.out"

    with open_to_stdin(in_path):
        data = list(map(int, input().split(' ')))
        print(fib_modified(data))

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected

