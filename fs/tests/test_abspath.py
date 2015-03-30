import os.path
import fs

from .setup import *

def test_abspath():
    assert fs.abspath(TEST_FILE) == os.path.abspath(TEST_FILE)