import os.path
import fs

from .setup import *

def test_normalize():
    path = '../test/'
    assert fs.normalize(path) == os.path.normpath(path)