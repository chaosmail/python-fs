import os
import os.path
import time
import pytest
import fs

from .setup import *

def test_touch_on_existing_file():

    before_time = time.ctime(os.path.getmtime(TEST_FILE))

    fs.touch(TEST_FILE)
    after_time = time.ctime(os.path.getmtime(TEST_FILE))

    assert after_time >= before_time

def test_touch_on_new_file():
    
    new_file = os.path.join(TEST_DIR, "new_file.txt")

    if (os.path.exists(new_file)):
        raise ValueError("File new_file.txt already exists!")

    fs.touch(new_file)

    assert os.path.exists(new_file) is True

    os.remove(new_file)


@pytest.mark.skipif(os.name == "nt", reason="does not work on windows")
def test_touch_on_directory():

    before_time = time.ctime(os.path.getmtime(TEST_DIR))

    fs.touch(TEST_DIR)
    after_time = time.ctime(os.path.getmtime(TEST_DIR))

    assert after_time >= before_time
