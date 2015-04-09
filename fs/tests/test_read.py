# coding: utf8

import os
import fs

from .setup import *


def test_read():

    content = "this is a test content"

    with open(TEST_FILE, 'w') as file:
        file.write(content)

    assert fs.read(TEST_FILE) == content


def test_read_utf8():

    content = u""""this is a test content with 
    utf-8 characters, such as ÀÁÂÂÄ or ¼½¾"""

    with open(TEST_FILE, 'wb') as file:
        file.write(content.encode('UTF-8'))

    assert fs.read(TEST_FILE) == content
