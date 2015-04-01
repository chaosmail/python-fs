import pytest
import os.path
import fs

from .setup import *

def test_rmdirs_directory():
    if (not os.path.exists(TEST_DIR_2)):
        raise ValueError("Folder %s does not exist!" % TEST_DIR_2)

    if (not os.path.exists(TEST_DIR_3)):
        raise ValueError("Folder %s does not exist!" % TEST_DIR_3)

    fs.rmdirs([TEST_DIR_2, TEST_DIR_3])

    assert os.path.exists(TEST_DIR_2) is False
    assert os.path.exists(TEST_DIR_3) is False