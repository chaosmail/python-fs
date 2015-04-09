import os.path
import fs

from .setup import *

def test_cwd():
    assert fs.cwd() == os.getcwd()