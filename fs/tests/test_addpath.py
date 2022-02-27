import fs
import pytest
import sys

from .setup import *


def test_addpath():
  TEST_MODULE = 'test_foo_bar.py'

  fs.touch(fs.join(TEST_DIR, TEST_MODULE))

  with pytest.raises(ImportError):
    import test_foo_bar

  fs.addpath(TEST_DIR)
  import test_foo_bar
  sys.path.remove(TEST_DIR)
  del sys.modules['test_foo_bar']

def test_addpath_not_existing_path():
  WRONG_TEST_DIR = 'foobartest'

  with pytest.raises(ValueError):
    fs.addpath(WRONG_TEST_DIR)
