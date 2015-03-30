import os
import fs

from .setup import *

def test_change_dir():

    cur = os.getcwd()

    if (cur == TEST_DIR):
        raise ValueError("Current working directory is already %s!" % TEST_DIR)

    fs.chdir(TEST_DIR)

    assert os.getcwd() == TEST_DIR

    # Switch back to the previous dir
    os.chdir(cur)
