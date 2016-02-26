import fs

from .setup import *


def test_add_suffix_to_filename():

    _filename = 'test.csv'
    _expected = 'test_suf.csv'

    assert _expected == fs.add_suffix(_filename, "_suf")


def test_add_suffix_to_filename_in_path():

    _filename = '/foo/bar/test.csv'
    _expected = '/foo/bar/test_suf.csv'

    assert _expected == fs.add_suffix(_filename, "_suf")


def test_add_suffix_to_path():

    _path = '/foo/bar/test'
    _expected = '/foo/bar/test_suf'

    assert _expected == fs.add_suffix(_path, "_suf")
