import os
import pytest
import subprocess


class BaseTest:

    def __init__(self, file):
        self.file = file

    def curpath(self):
        pth, _ = os.path.split(os.path.abspath(self.file))
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

    # def test_in_validate_out(self, test_name, test_id):
    #     """
    #
    #     :param test_name:
    #     :param test_id:
    #     :return:
    #     """
    #     in_path, out_path, script_path = self.file_paths_for_tests(test_name, test_id)
    #     print("\n"+"-"*50)
    #     print("Calling %s" % script_path)
    #     print("input file %s" % in_path)
    #     test_data = open(in_path, "r")
    #     expected = open(out_path, "r").read()
    #     proc = subprocess.Popen('python ' + script_path, shell=True, stdin=test_data, stdout=subprocess.PIPE)
    #     out = proc.communicate()[0].decode("utf-8")
    #     assert expected == out
    #     print("\n"+"-"*50)
