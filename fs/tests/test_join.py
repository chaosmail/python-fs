import os
import fs

from .setup import *

def test_join_arguments():
    assert fs.join(os.sep, 'etc', 'var') == os.sep + 'etc' + os.sep + 'var'
    assert fs.join(os.sep, 'etc', 'var/') == os.sep + 'etc' + os.sep + 'var/'

def test_join_array():
    assert fs.join([os.sep, 'etc', 'var']) == os.sep + 'etc' + os.sep + 'var'
    assert fs.join([os.sep, 'etc', 'var/']) == os.sep + 'etc' + os.sep + 'var/'