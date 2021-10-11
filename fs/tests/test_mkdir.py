import os.path
import pytest
import fs
import unittest

from .setup import *

def test_mkdir():

    dir_name = "foo"
    path = os.path.join(TEST_DIR, dir_name)

    if (os.path.exists(path)):
        raise ValueError("Directory %s already exists!" % path)

    fs.mkdir(path)

    assert os.path.exists(path) is True
    os.rmdir(path)

def test_mkdir_recursive():

    dir_name = "foo/bar/baz"
    path = os.path.join(TEST_DIR, dir_name)

    if (os.path.exists(path)):
        raise ValueError("Directory %s already exists!" % path)

    fs.mkdir(path)

    assert os.path.exists(path) is True
    os.removedirs(path)

def test_mkdir_recursive_fail():

    dir_name = "foo/bar/bal"
    path = os.path.join(TEST_DIR, dir_name)

    if (os.path.exists(path)):
        raise ValueError("Directory %s already exists!" % path)

    with pytest.raises(FileNotFoundError):
        fs.mkdir(path, recursive=False)