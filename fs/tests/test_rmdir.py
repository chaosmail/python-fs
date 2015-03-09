import pytest
import os
import shutil

import fs

DIR = os.path.dirname(os.path.realpath(__file__))
TEST_DIR = os.path.join(DIR, "test_dir")
TEST_DIR_2 = os.path.join(TEST_DIR, "test_dir_2")
TEST_DIR_3 = os.path.join(TEST_DIR, "test_dir_3")
TEST_FILE = os.path.join(TEST_DIR, "test_file.txt")

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    pass

def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    # Remove test directory
    if (os.path.exists(TEST_DIR)):
        shutil.rmtree(TEST_DIR)

def setup_function(function):
    """ setup any state specific to the execution of the given function."""
    # Create test directory
    os.makedirs(TEST_DIR, exist_ok=True)
    os.makedirs(TEST_DIR_2, exist_ok=True)
    os.makedirs(TEST_DIR_3, exist_ok=True)
    
    # Create a test file
    open(TEST_FILE, 'w+').close()

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    method.
    """
    pass

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

    with pytest.raises(NotADirectoryError):
        fs.rmdir(TEST_FILE)

    assert os.path.exists(TEST_FILE) is True