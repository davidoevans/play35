import os
import pytest
import subprocess


def pytest_generate_tests(metafunc):
    """
    As per Test Scenarios described in http://pytest.org/2.2.4/example/parametrize.html
    :return:
    """
    idlist = []
    argvalues = []
    for scenario in metafunc.cls.scenarios:
        idlist.append(scenario[0])
        items = scenario[1].items()
        argnames = [x[0] for x in items]
        argvalues.append(([x[1] for x in items]))
    metafunc.parametrize(argnames, argvalues, ids=idlist)

scenario1 = ('sample', {'test_name': 'fibonacci_modified', 'test_id': 'sample'})
scenario5 = ('5', {'test_name': 'fibonacci_modified', 'test_id': '5'})


class TestFibonacciModifiedWithScenarios:
    scenarios = [scenario1, scenario5]

    # def __init__(self):
    #     super().__init__(self, __file__)


    def curpath(self):
        pth, _ = os.path.split(os.path.abspath(__file__))
        return pth

    def file_paths_for_tests(self, test_name, test_number="sample"):
        """
        Generate the input file, output file, and script paths to be used in a test assuming the script to be
        tested and the data to be used for testing are both parallel to this test script.

        :param test_name:
        :param test_number:
        :return:
        """
        print(os.path.join(self.curpath()))
        data_path = self.curpath().replace("tests/", "tests/data/")
        parallel_path = self.curpath().replace("tests/", "")
        data_path = os.path.join(data_path, test_name + "_" + str(test_number))
        script_path = os.path.join(parallel_path, test_name + ".py")
        return data_path + ".in", data_path + ".out", script_path

    # # @pytest.mark.parametrize(("test_name", "test_id"), [
    # #     ("anagram", "sample"),
    # #     ("anagram", "1"),
    # # ])
    def test_in_validate_out(self, test_name, test_id):
        """

        :param test_name:
        :param test_id:
        :return:
        """
        in_path, out_path, script_path = self.file_paths_for_tests(test_name, test_id)
        print("\n"+"-"*50)
        print("Calling %s" % script_path)
        print("input file %s" % in_path)
        test_data = open(in_path, "r")
        expected = open(out_path, "r").read()
        proc = subprocess.Popen('python ' + script_path, shell=True, stdin=test_data, stdout=subprocess.PIPE)
        out = proc.communicate()[0].decode("utf-8")
        assert expected == out
        print("\n"+"-"*50)


    # def func1(s):
    #     print("hello")
    #     print("dubdu")
    #     print(s)

    # @pytest.mark.parametrize(("filename_expected", "function_to_test", "args_for_function"), [
    #     ("data/anagram_2.out", make_anagram, 'aaabbb'),
    #     ("data/func_1.out", func1, 'aaa'),
    # ])
    # def test_funcoutput(capfd, filename_expected, function_to_test, args_for_function):
    #     function_to_test(args_for_function)
    #     resout, reserr = capfd.readouterr()
    #     expected = open(os.path.join(curpath(), filename_expected), "r").read()
    #     assert resout == expected

# if __name__ == "__main__":
#     test = AnagramTest()
#     test.test_in_validate_out
