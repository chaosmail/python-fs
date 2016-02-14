import fs

from .setup import *

def test_basename_from_path():

    _filename = 'test'
    _ext = ".txt"
    _file = "foo/bar/%s%s" % (_filename, _ext)
    _base = fs.basename(_file)

    assert _base == "%s%s" % (_filename, _ext)

def test_basename_from_file():

    _filename = 'test'
    _ext = ".txt"
    _file = "%s%s" % (_filename, _ext)
    _base = fs.basename(_file)

    assert _base == "%s%s" % (_filename, _ext)

def test_basename_strip_ext():

    _filename = 'test'
    _ext = ".txt"
    _file = "foo/bar/%s%s" % (_filename, _ext)
    _base = fs.basename(_file, ext=_ext)

    assert _base == "%s" % _filename

def test_basename_autostrip_ext():

    _filename = 'test'
    _ext = ".txt"
    _file = "foo/bar/%s%s" % (_filename, _ext)
    _base = fs.basename(_file, ext=False)

    assert _base == "%s" % _filename