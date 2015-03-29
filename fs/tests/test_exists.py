import os.path
import fs

from .setup import *

def test_exists_dir():
    assert fs.exists(TEST_DIR) is True

def test_not_exists_dir():
    assert fs.exists(os.path.join(TEST_DIR, "foo")) is False

def test_exists_file():
    assert fs.exists(TEST_FILE) is True

def test_not_exists_dir():
    assert fs.exists(os.path.join(TEST_DIR, "foo.txt")) is False