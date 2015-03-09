import pytest
import os
import time
import shutil

import fs

DIR = os.path.dirname(os.path.realpath(__file__))
TEST_DIR = os.path.join(DIR, "test_dir")
TEST_FILE = os.path.join(TEST_DIR, "test_file.txt")

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    pass

def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    # Remove test directory
    shutil.rmtree(TEST_DIR)

def setup_function(function):
    """ setup any state specific to the execution of the given function."""
    # Create test directory
    os.makedirs(TEST_DIR, exist_ok=True)
    
    # Create a test file
    open(TEST_FILE, 'w+').close()

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    method.
    """
    pass

def test_touch_on_existing_file():

    before_time = time.ctime(os.path.getmtime(TEST_FILE))

    fs.touch(TEST_FILE)
    after_time = time.ctime(os.path.getmtime(TEST_FILE))

    assert after_time >= before_time

def test_touch_on_new_file():
    
    new_file = os.path.join(TEST_DIR, "new_file.txt")

    if (os.path.exists(new_file)):
        raise ValueError("File new_file.txt already exists!")

    fs.touch(new_file)

    assert os.path.exists(new_file) is True