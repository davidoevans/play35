"""
# Overview
This module is intended to provide a test harness that mimics the behaviour seen on the hackerrank site.  Using
this harness enables localized testing of the hackerrank challenges and the resulting code can be posted
verbatum to the hackerrank site.

The general behaviour goes as follows:

* test data is read from a input file
* each line test data is received via STDIN using input()
* results are written to STDOUT
* STDOUT is captured and validated against file containing the expected output

By default this, the script to be tested as well as the input and output data are assumed to be in a
directory/package structure parallel to the test script.

* test_path - tests/<path_to_test_script>
* module_to_test - <path_to_test_script>
* input data - data/<path_to_test_script>/<test_name>_<test_id>.in
* output data - data/<path_to_test_script>/<test_name>_<test_id>.out

# Limitations of this implementation
1. Cannot debug the script during testing. Attempts to set breakpoints in an IDE will not be recognized and
programatically inserting interupts using `IPython.core.debugger` will cause test failure.  This is due to the
fact that the script to be tested is executed as a `subprocess`.
2. Only supports the parallel directory structure described above.
3. Sloppy and likely poor use of inheritance.
4. Test that inherit from BaseTest consist of duplicate copy/paste implementations.

"""
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


class BaseTest:
    """
    This is meant to provide a test harness for
    """
    def __init(self, filename=__file__):
        self.filename = filename

    def curpath(self):
        pth, _ = os.path.split(os.path.abspath(self.filename))
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

    def test_in_validate_out(self, test_name, test_id):
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

