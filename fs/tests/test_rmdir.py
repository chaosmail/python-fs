import pytest
import os.path
import fs

from .setup import *

def test_rmdir_directory():
    if (not os.path.exists(TEST_DIR_3)):
        raise ValueError("Folder test_dir/test_dir_3/ does not exist!")

    fs.rmdir(TEST_DIR_3)

    assert os.path.exists(TEST_DIR_3) is False

def test_rmdir_directory_recursive():
    if (not os.path.exists(TEST_DIR)):
        raise ValueError("Folder test_dir/ does not exist!")

    fs.rmdir(TEST_DIR)

    assert os.path.exists(TEST_DIR) is False

def test_rmdir_file():
    if (not os.path.exists(TEST_FILE)):
        raise ValueError("File test_dir/test_file.txt does not exist!")

    try:
        with pytest.raises(NotADirectoryError):
            fs.rmdir(TEST_FILE)
    except NameError as e:
        with pytest.raises(OSError):
            fs.rmdir(TEST_FILE)

    assert os.path.exists(TEST_FILE) is True