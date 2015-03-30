import os.path
import fs

from .setup import *

def test_truncate_dir():

    if (not os.path.exists(TEST_DIR_2)):
        raise ValueError("Directory %s does not exist!" % TEST_DIR_2)

    if (not os.path.exists(TEST_FILE)):
        raise ValueError("File %s does not exist!" % TEST_FILE)

    fs.truncate(TEST_DIR)

    assert os.path.exists(TEST_DIR) is True
    assert os.path.exists(TEST_FILE) is False
    assert os.path.exists(TEST_DIR_2) is False
