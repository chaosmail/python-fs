# coding: utf8
from __future__ import unicode_literals
import os
import fs
import pickle

from .setup import *


def test_put():

    obj = [1,2,3,4,5,'test']

    fs.put(TEST_FILE, obj)

    with open(TEST_FILE, 'rb') as file:
        content = pickle.load(file)

    assert obj == content
