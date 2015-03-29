import os.path
import fs

from .setup import *

def test_isfile_on_existing_file():
    assert fs.isfile(TEST_FILE) is True

def test_isfile_on_non_existing_file():
    assert fs.isfile(os.path.join(TEST_DIR, "foo.txt")) is False

def test_isfile_on_existing_directory():
    assert fs.isfile(TEST_DIR) is False

def test_isfile_on_non_existing_directory():
    assert fs.isfile(os.path.join(TEST_DIR, "foo")) is False