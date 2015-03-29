import os
import shutil

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
    if (not os.path.exists(TEST_DIR)):
        os.makedirs(TEST_DIR)
    if (not os.path.exists(TEST_DIR_2)):
        os.makedirs(TEST_DIR_2)
    if (not os.path.exists(TEST_DIR_3)):
        os.makedirs(TEST_DIR_3)
    
    # Create a test file
    open(TEST_FILE, 'w+').close()

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    method.
    """
    pass