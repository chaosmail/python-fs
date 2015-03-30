import os
import fs

from .setup import *

def test_sep():
    assert fs.sep == os.sep