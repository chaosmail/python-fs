# coding: utf8
from __future__ import unicode_literals
import os
import fs
import pickle

from .setup import *


def test_get():

    obj = [1,2,3,4,5,'test']

    with open(TEST_FILE, 'wb') as file:
        pickle.dump(obj, file)

    assert obj == fs.get(TEST_FILE)
