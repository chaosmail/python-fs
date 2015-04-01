import os
import os.path
import fs

from .setup import *

def test_listdirs():
    
    dirs = [ os.path.join(TEST_DIR,f) for f in os.listdir(TEST_DIR) 
    	if os.path.isdir(os.path.join(TEST_DIR,f)) ]

    fs_dirs = list( fs.listdirs(TEST_DIR) )

    assert len(dirs) is len(fs_dirs)
    assert sorted(dirs) == sorted(fs_dirs)