import os
import os.path
import fs

from .setup import *

def test_find():
    
    files = [] 
    for root, dirnames, filenames in os.walk(TEST_DIR):
        for f in filenames:
            if os.path.isfile(os.path.join(TEST_DIR,f)):
                if fs.extname(f) == '.txt':
                    files.append(os.path.join(TEST_DIR,f)) 

    fs_files = list( fs.find('*.txt', TEST_DIR) )

    assert len(files) > 0
    assert len(files) is len(fs_files)
    assert sorted(files) == sorted(fs_files)

def test_find_not_recursive():
    
    files = [f for f in list(fs.list(TEST_DIR)) if fs.extname(f) == '.txt']
    fs_files = list( fs.find('*.txt', TEST_DIR, recursive=False) )

    assert len(files) > 0
    assert len(files) is len(fs_files)
    assert sorted(files) == sorted(fs_files)