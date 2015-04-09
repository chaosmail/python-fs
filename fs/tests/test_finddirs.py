import os
import re
import os.path
import fs

from .setup import *

def test_finddirs():
    
    dirs = [] 
    for root, dirnames, filenames in os.walk(TEST_DIR):
        for d in dirnames:
            if os.path.isdir(os.path.join(TEST_DIR,d)):
                if re.search('_3$', d):
                    dirs.append(os.path.join(TEST_DIR,d)) 

    fs_dirs = list( fs.finddirs('*_3', TEST_DIR) )

    assert len(dirs) > 0
    assert len(dirs) is len(fs_dirs)
    assert sorted(dirs) == sorted(fs_dirs)


def test_finddirs_not_recursive():
    
    dirs = [d for d in list(fs.listdirs(TEST_DIR)) if re.search('_3$', d)]
    fs_dirs = list( fs.finddirs('*_3', TEST_DIR, recursive=False) )

    assert len(dirs) > 0
    assert len(dirs) is len(fs_dirs)
    assert sorted(dirs) == sorted(fs_dirs)