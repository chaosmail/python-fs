# coding: utf8
from __future__ import unicode_literals
import os
import fs

from .setup import *


def test_write():

    write_content = "test content"
    fs.write(TEST_FILE, write_content)

    with open(TEST_FILE, 'r') as file:
        content = file.read()

    assert write_content == content


def test_write_utf8():

    write_content = """"this is a test content with 
    utf-8 characters, such as ÀÁÂÂÄ or ¼½¾"""

    fs.write(TEST_FILE, write_content)

    with open(TEST_FILE, 'rb') as file:
        content = file.read()

    assert write_content == content.decode('UTF-8')