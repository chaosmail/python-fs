import fs
import pytest

from .setup import *


def test_addpath():
  TEST_MODULE = 'test_foo_bar.py'

  fs.touch(fs.join(TEST_DIR, TEST_MODULE))

  with pytest.raises(ImportError):
    import test_foo_bar

  fs.addpath(TEST_DIR)
  import test_foo_bar