import pytest
import os


def curpath():
    pth, _ = os.path.split(os.path.abspath(__file__))
    return pth


def test_path():
    print("\n" + "-"*50)
    print(curpath())
    print(type(curpath()))
    print(os.path.join(curpath(), 'data/func_1.out'))