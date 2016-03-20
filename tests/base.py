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
* if sticking with inheritance, consider using @abstractmethod
* use composition instead?
* create a mixin instead?  (i.e. TestPathMixin)
*
* other?
4. Test that inherit from BaseTest consist of duplicate copy/paste implementations.
5. Required to create an import that appears unused.
* `from tests.base.base_test import pytest_generate_tests`
"""

import os
import sys
import subprocess
import contextlib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))[:-5]


@contextlib.contextmanager
def open_to_stdin(filename):
    """
    This context manager opens a file and yields it's content to STDIN.  Within this context, lines of the file
    can be accessed using `input()` calls.

    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        sys.stdin = f
        try:
            yield sys.__stdin__
        except EOFError:
            pass

class TestPathMixin:

    def current_path(self, filename):
        pth, _ = os.path.split(os.path.abspath(filename))
        return pth

    def data_path(self, filename, test_name, data_type='input', data_path=None, test_id="sample"):
        if data_path:
            data_path = self.current_path(filename).replace("tests/", "tests/data/")
        else:
            data_path = ""
            
        data_path = os.path.join(data_path, test_name + "_" + str(test_id))
        return data_path + ".in" if data_type == "input" else ".out"

    def script_path(self, filename, test_name):
        parallel_path = self. current_path(filename).replace("tests/", "")
        script_path = os.path.join(parallel_path, test_name + ".py")
        return script_path

    def file_paths_for_tests(self, test_name, test_number="sample"):
        """
        Generate the input file, output file, and script paths to be used in a test assuming the script to be
        tested and the data to be used for testing are both parallel to this test script.

        :param test_name:
        :param test_number:
        :return:
        """
        print(os.path.join(self.current_path()))
        data_path = self.current_path().replace("tests/", "tests/data/")
        data_path = os.path.join(data_path, test_name + "_" + str(test_number))
        parallel_path = self. current_path().replace("tests/", "")
        script_path = os.path.join(parallel_path, test_name + ".py")
        return data_path + ".in", data_path + ".out", script_path

