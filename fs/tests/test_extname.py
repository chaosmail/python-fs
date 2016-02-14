import fs

from .setup import *

def test_extname_from_path():

    _filename = 'test'
    _ext = ".txt"
    _file = "foo/bar/%s%s" % (_filename, _ext)
    _extname = fs.extname(_file)

    assert _extname == _ext

def test_extname_from_file():

    _filename = 'test'
    _ext = ".txt"
    _file = "%s%s" % (_filename, _ext)
    _extname = fs.extname(_file)

    assert _extname == _ext