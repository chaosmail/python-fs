import pytest
import os.path
import fs

from .setup import *

def test_rm_file():
    if (not os.path.exists(TEST_FILE)):
        raise ValueError("File %s does not exist!" % TEST_FILE)

    if (not os.path.exists(TEST_FILE_2)):
        raise ValueError("File %s does not exist!" % TEST_FILE_2)

    fs.rmfiles([TEST_FILE, TEST_FILE_2])

    assert os.path.exists(TEST_FILE) is False
    assert os.path.exists(TEST_FILE_2) is False