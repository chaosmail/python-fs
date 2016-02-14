import fs

from .setup import *

def test_dirname_from_file():

    _file = 'test.txt'
    _dir = "foo/bar"
    _path = "%s/%s" % (_dir, _file)
    _dirname = fs.dirname(_path)

    assert _dirname == _dir

def test_dirname_from_dir():

    _dir1 = "foo"
    _dir = "%s/bar" % _dir1
    _dirname = fs.dirname(_dir)

    assert _dirname == _dir1