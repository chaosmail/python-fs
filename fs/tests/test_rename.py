import os.path
import fs

from .setup import *

def test_rename_file():

    rename_to = "test_rename.txt"
    rename_file = os.path.join(TEST_DIR, rename_to)

    if (os.path.exists(rename_file)):
        raise ValueError("File %s already exists!" % rename_file)

    fs.rename(TEST_FILE, rename_file)

    assert os.path.exists(rename_file) is True

def test_rename_directory():

    rename_to = "test_rename"
    rename_dir = os.path.join(TEST_DIR, rename_to)

    if (os.path.exists(rename_dir)):
        raise ValueError("Directory %s already exists!" % rename_dir)

    fs.rename(TEST_DIR_2, rename_dir)

    assert os.path.exists(rename_dir) is True