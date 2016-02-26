import fs

from .setup import *


def test_add_prefix_to_filename():

    _filename = 'test.csv'
    _expected = 'pre_test.csv'

    assert _expected == fs.add_prefix(_filename, "pre_")


def test_add_prefix_to_filename_in_path():

    _filename = '/foo/bar/test.csv'
    _expected = '/foo/bar/pre_test.csv'

    assert _expected == fs.add_prefix(_filename, "pre_")


def test_add_prefix_to_path():

    _path = '/foo/bar/test'
    _expected = '/foo/bar/pre_test'

    assert _expected == fs.add_prefix(_path, "pre_")
