import os
import os.path
import fs

from .setup import *

def test_list():
    
    files = [ os.path.join(TEST_DIR,f) for f in os.listdir(TEST_DIR) 
        if os.path.isfile(os.path.join(TEST_DIR,f)) ]

    fs_files = list( fs.list(TEST_DIR) )

    assert len(files) is len(fs_files)
    assert sorted(files) == sorted(fs_files)