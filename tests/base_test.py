import os
import sys
from tests.base import TestPathMixin
from tests.base import open_to_stdin

BASE_DIR = os.path.dirname(os.path.dirname(__file__))[:-5]


def test_test_path_mixin():
    tpm = TestPathMixin()
    print(tpm.data_path(__file__, "the_test"))


def test_capsys_fixture(capsys): # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"
    print("next")
    out, err = capsys.readouterr()
    assert out == "next\n"
    print("hihi")
    print("hoho")
    out, err = capsys.readouterr()
    print(out)
    assert out == "hihi\nhoho\n"


def test_open_to_stdin():
    in_path = BASE_DIR + "tests/data/practice/hackerrank/algorithms/implementation/grid_search_sample.in"
    with open_to_stdin(in_path) as f:
        while f:
            print("line: %s" % input())

