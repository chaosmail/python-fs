import os
import fs

from .setup import *

def test_write():

    write_content = "test content"
    fs.write(TEST_FILE, write_content)

    with open(TEST_FILE, 'r') as file:
        content = file.read()

    assert write_content == content
