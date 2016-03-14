from practice.inheritance.parent import Parent

class Child(Parent):
    """
    nothing
    """


if __name__ == "__main__":
    child = Child()
    child.current_path()
    print(child.file_paths_for_tests('sample'))