import pytest
from practice.hackerrank.algorithms.implementation import grid_search
from practice.hackerrank.algorithms.implementation import utopian_tree
from practice.hackerrank.algorithms.implementation import decent_number
from tests.base import open_to_stdin

BASE_DIR = "/Users/davidevans/PycharmProjects/play35/"


@pytest.mark.parametrize("in_data,out_data",
                         [("tests/data/practice/hackerrank/algorithms/implementation/decent_number_2.in",
                           "tests/data/practice/hackerrank/algorithms/implementation/decent_number_2.out"),
                          ("tests/data/practice/hackerrank/algorithms/implementation/decent_number_sample.in",
                           "tests/data/practice/hackerrank/algorithms/implementation/decent_number_sample.out"),
                          ])
def test_decent_number(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data
    with open_to_stdin(in_path):
        t = int(input().strip())
        for a0 in range(t):
            n = int(input().strip())
            dn = decent_number(n)
            if dn:
                print(dn)

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected


@pytest.mark.parametrize("in_data, out_data",
                         [("tests/data/practice/hackerrank/algorithms/implementation/grid_search_sample.in",
                           "tests/data/practice/hackerrank/algorithms/implementation/grid_search_sample.out"),
                          ("tests/data/practice/hackerrank/algorithms/implementation/grid_search_7.in",
                           "tests/data/practice/hackerrank/algorithms/implementation/grid_search_7.out")
                          ])
def test_grid_search(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data
    with open_to_stdin(in_path):
        t = int(input().strip())
        for a0 in range(t):
            R, C = input().strip().split(' ')
            R, C = [int(R), int(C)]
            G = []
            G_i = 0
            for G_i in range(R):
                G_t = str(input().strip())
                G.append(G_t)
            r, c = input().strip().split(' ')
            r, c = [int(r), int(c)]
            P = []
            P_i = 0
            for P_i in range(r):
                P_t = str(input().strip())
                P.append(P_t)

            print(grid_search(P, G))

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected


@pytest.mark.parametrize("in_data, out_data",
                         [("tests/data/practice/hackerrank/algorithms/implementation/utopian_tree_sample.in",
                           "tests/data/practice/hackerrank/algorithms/implementation/utopian_tree_sample.out")
                          ])
def test_utopian_tree(capsys, in_data, out_data):
    in_path = BASE_DIR + in_data
    out_path = BASE_DIR + out_data
    with open_to_stdin(in_path):
        t = int(input().strip())
        for a0 in range(t):
            n = int(input().strip())
            print(utopian_tree(n))

    out, err = capsys.readouterr()
    expected = open(out_path, "r").read()
    assert out == expected
