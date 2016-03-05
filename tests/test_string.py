import os
import pytest
import fileinput
import subprocess
# from practice.string.anagram import make_anagram


def curpath():
    pth, _ = os.path.split(os.path.abspath(__file__))
    return pth


def file_paths_for_tests(test_name, test_number="sample"):
    data_path = os.path.join(curpath(), "data/" + test_name + "_" + str(test_number))
    script_path = os.path.join(curpath(), "../practice/string/" + test_name + ".py")
    return data_path + ".in", data_path + ".out", script_path

@pytest.mark.parametrize(("test_name"), [
    ("anagram"),
])
def toast_in_out(capfd, test_name):
    in_path, out_path, script_path = file_paths_for_tests(test_name)
    print("\n"+"-"*50)
    print("in_path %s" % in_path)
    print("out_path %s" % out_path)
    with fileinput.input(in_path) as f:
        for line in f:
            print(f.filename(), f.lineno(), line, end='')


@pytest.mark.parametrize(("test_name", "test_id"), [
    ("anagram", "sample"),
    ("anagram", "1"),
])
def test_process(capfd, test_name, test_id):
    in_path, out_path, script_path = file_paths_for_tests(test_name, test_id)
    print("\n"+"-"*50)
    print("Calling %s" % script_path)
    print("input file %s" % in_path)
    test_data = open(in_path, "r")
    expected = open(out_path, "r").read()
    proc = subprocess.Popen('python ' + script_path, shell=True, stdin=test_data, stdout=subprocess.PIPE)
    out = proc.communicate()[0].decode("utf-8")
    assert expected == out
    print("\n"+"-"*50)


def func1(s):
    print("hello")
    print("dubdu")
    print(s)

# @pytest.mark.parametrize(("filename_expected", "function_to_test", "args_for_function"), [
#     ("data/anagram_2.out", make_anagram, 'aaabbb'),
#     ("data/func_1.out", func1, 'aaa'),
# ])
# def test_funcoutput(capfd, filename_expected, function_to_test, args_for_function):
#     function_to_test(args_for_function)
#     resout, reserr = capfd.readouterr()
#     expected = open(os.path.join(curpath(), filename_expected), "r").read()
#     assert resout == expected


@pytest.fixture()
def anagram_data():
    return 'hi'


def test1(anagram_data):
    assert anagram_data == 'hi'


# def test_make_anagram():
#     assert make_anagram('aaabbb') == 3
#     assert make_anagram('aaabbc') == 3

