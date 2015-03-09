def isfile(path):
    """Check if *path* is a file"""
    import os.path
    return os.path.isfile(path)

def isdir(path):
    """Check if *path* is a directory"""
    import os.path
    return os.path.isdir(path)

def rename(oldPath, newPath):
    import os
    return os.rename(oldPath, newPath)

def truncate(path):
    pass

def chown(path):
    pass

def chmod(path, mode):
    pass

def link(srcPath, destPath):
    pass

def symlink(srcPath, destPath, type):
    pass

def realpath(path):
    pass

def unlink(path):
    """Unix equivalent *unlink*
    Remove the file *path*"""
    import os
    return os.unlink(path)

def rmdir(path, recursive=True, ignore_errors=False):
    """Remove the directory *path*"""
    if recursive:
        import shutil
        return shutil.rmtree(path, ignore_errors=ignore_errors)
    else:
        import os
        return os.remdir(path)

def rm(path, **kwargs):
    """Remove *path* which can be either a file
    or a directory"""
    if isfile(path):
        unlink(path, **kwargs)
    else:
        rmdir(path, **kwargs)

def mkdir(path, recursive=True):
    pass

def touch(path, mode=0o666):
    """Unix equivalent *touch*
    @src: http://stackoverflow.com/a/1160227"""
    import os
    flags = os.O_CREAT | os.O_APPEND
    with os.fdopen(os.open(path, flags=flags, mode=mode)) as f:
        os.utime(f.fileno() if os.utime in os.supports_fd else path,
            dir_fd=None if os.supports_fd else dir_fd)

def exists(path):
    """Check if file or directory exists"""
    import os.path
    return os.path.exists(path)

def access(path, mode):
    pass