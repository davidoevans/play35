from practice.inheritance.parent import Parent


class Child(Parent):

    def __init__(self):
        """
        Do nothing
        :return:
        """
        super().__init__(__file__)


if __name__ == "__main__":
    child = Child()
    child.current_path()
    print(child.file_paths_for_tests('sample'))
