"""
These are notes and code snippets from:
https://www.codementor.io/python/tutorial/essential-python-interview-questions#/.VrlnI0xL6Q8.gmail

"""
# Python is dynamically typed; meaning:
a = 255
a = "I am making 'a' a new type"

def print_directory_contents(sPath):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
