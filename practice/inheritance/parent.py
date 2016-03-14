import os

class Parent:

    def __init__(self, filename=__file__):
        self.filename = filename
        """
        :return:
        """

    def current_path(self):
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
        data_path = self.current_path().replace("tests/", "tests/data/")
        parallel_path = self.current_path().replace("tests/", "")
        data_path = os.path.join(data_path, test_name + "_" + str(test_number))
        script_path = os.path.join(parallel_path, test_name + ".py")
        return data_path + ".in", data_path + ".out", script_path


if __name__ == "__main__":
    parent = Parent()
    print(parent.current_path())
    print(parent.file_paths_for_tests('sample'))
