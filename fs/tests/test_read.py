import os
import fs

from .setup import *

def test_read():

    with open(TEST_FILE, 'r') as file:
        content = file.read()

    assert fs.read(TEST_FILE) == content
