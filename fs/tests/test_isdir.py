import os.path
import fs

from .setup import *

def test_isdir_on_existing_file():
    assert fs.isdir(TEST_FILE) is False

def test_isdir_on_non_existing_file():
    assert fs.isdir(os.path.join(TEST_DIR, "foo.txt")) is False

def test_isdir_on_existing_directory():
    assert fs.isdir(TEST_DIR) is True

def test_isdir_on_non_existing_directory():
    assert fs.isdir(os.path.join(TEST_DIR, "foo")) is False