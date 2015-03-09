import pytest
import os
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

def test_isdir_on_existing_file():

    assert fs.isdir(TEST_FILE) is False

def test_isdir_on_non_existing_file():

    assert fs.isdir(os.path.join(TEST_DIR, "foo.txt")) is False

def test_isdir_on_existing_directory():

    assert fs.isdir(TEST_DIR) is True

def test_isdir_on_non_existing_directory():

    assert fs.isdir(os.path.join(TEST_DIR, "foo")) is False