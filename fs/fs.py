
import os

"""Constants"""

OPEN_FUNC = open
sep = os.sep
try:
    import types
    LIST_TYPE = types.ListType
except Exception:
    LIST_TYPE = list

    
"""Helper Functions"""

def _is_list(e):
    """retruns true if *e* is a list type"""
    return isinstance(e, LIST_TYPE)

def _to_list(e):
    """returns always a list containing *e*"""
    return e if _is_list(e) else [e]


"""Filesystem Methods"""

def isfile(path, **kwargs):
    """Check if *path* is a file"""
    import os.path
    return os.path.isfile(path, **kwargs)

def isdir(path, **kwargs):
    """Check if *path* is a directory"""
    import os.path
    return os.path.isdir(path, **kwargs)

def rename(oldPath, newPath, **kwargs):
    """rename the file oldPath to newPath"""
    import os
    return os.rename(oldPath, newPath, **kwargs)

def truncate(path, **kwargs):
    """remove all files and directories 
    from a directory *path*"""
    rmfiles(list(path))
    rmdirs(listdirs(path))

def chdir(path, **kwargs):
    """Change current working directory"""
    import os
    return os.chdir(path, **kwargs)

def chown(path):
    pass

def chmod(path, mode):
    pass

def link(srcPath, destPath):
    pass

def symlink(srcPath, destPath, type):
    pass

def stat(path):
    """Return file stats"""
    import os
    return os.stat(path)

def ctime(path):
    """platform dependent; time of most recent metadata change on Unix, or the time of creation on Windows"""
    return stat(path).st_ctime

def atime(path):
    """Return time of most recent access"""
    return stat(path).st_atime

def mtime(path):
    """time of most recent content modification"""
    return stat(path).st_mtime

def abspath(path, **kwargs):
    """Return the absolute path of *path*"""
    import os.path
    return os.path.abspath(path, **kwargs)

def normalize(path, **kwargs):
    """Return the normalized path of *path*"""
    import os.path
    return os.path.normpath(path, **kwargs)

def rm(path, **kwargs):
    """Remove the file *path*"""
    import os
    return os.unlink(path, **kwargs)

def unlink(*args, **kwargs):
    """Unix equivalent *unlink*"""
    return rm(*args, **kwargs)

def rmdir(path, recursive=True, **kwargs):
    """Remove the directory *path*"""
    if recursive:
        import shutil
        return shutil.rmtree(path, **kwargs)
    else:
        import os
        return os.remdir(path, **kwargs)

def rmfiles(paths, **kwargs):
    """Remove an array of files *path*"""
    for p in paths:
        rm(p, **kwargs)

def rmdirs(paths, **kwargs):
    """Remove an array of files *path*"""
    for p in paths:
        rmdir(p, **kwargs)

def mkdir(path, recursive=True, **kwargs):
    """Unix equivalent *mkdir*"""
    import os
    if recursive:
        os.makedirs(path, **kwargs)
    else:
        os.mkdir(path, **kwargs)

def touch(path):
    """Unix equivalent *touch*
    @src: http://stackoverflow.com/a/1158096"""
    import os
    try:
        OPEN_FUNC(path, 'a+').close()
    except IOError:
        os.utime(path, None)

def exists(path, **kwargs):
    """Check if file or directory exists"""
    import os.path
    return os.path.exists(path, **kwargs)

def access(path, **kwargs):
    pass

def list(path='.'):
    """generator that returns all files of *path*"""
    import os
    for f in os.listdir(path):
        if isfile(join(path, f)):
            yield join(path, f) if path != '.' else f

def listdirs(path='.'):
    """generator that returns all directories of *path*"""
    import os
    for f in os.listdir(path):
        if isdir(join(path, f)):
            yield join(path, f) if path != '.' else f

def find(pattern, path='.', exclude=None, recursive=True):
    """Find files that match *pattern* in *path*"""
    import fnmatch
    import os
    
    if recursive:
        for root, dirnames, filenames in os.walk(path):
            for pat in _to_list(pattern):
                for filename in fnmatch.filter(filenames, pat):
                    filepath = join(abspath(root), filename)
                    for excl in _to_list(exclude):
                        if excl and fnmatch.fnmatch(filepath, excl):
                            break
                    else:
                        yield filepath
    else:
        for pat in _to_list(pattern):
            for filename in fnmatch.filter(list(path), pat):
                filepath = join(abspath(path), filename)
                for excl in _to_list(exclude):
                    if excl and fnmatch.fnmatch(filepath, excl):
                        break
                    else:
                        yield filepath

def finddirs(pattern, path='.', exclude=None, recursive=True):
    """Find directories that match *pattern* in *path*"""
    import fnmatch
    import os
    if recursive:
        for root, dirnames, filenames in os.walk(path):
            for pat in _to_list(pattern):
                for dirname in fnmatch.filter(dirnames, pat):
                    dirpath = join(abspath(root), dirname)
                    for excl in _to_list(exclude):
                        if excl and fnmatch.fnmatch(dirpath, excl):
                            break
                    else:
                        yield dirpath
    else:
        for pat in _to_list(pattern):
            for dirname in fnmatch.filter(listdirs(path), pat):
                dirpath = join(abspath(path), dirname)
                for excl in _to_list(exclude):
                    if excl and fnmatch.fnmatch(dirpath, excl):
                        break
                else:
                    yield dirpath

def open(path, mode='r', **kwargs):
    """Open *content* to file *path*"""
    return OPEN_FUNC(path, mode, **kwargs)

def write(path, content, encoding="UTF-8", append=False, raw=False):
    """Write *content* to file *path*"""
    mode = 'wb' if not append else 'ab'
    with OPEN_FUNC(path, mode) as _file:
        if raw:
            import shutil
            shutil.copyfileobj(content, _file)
        else:
            _file.write(content.encode(encoding))

def read(path, encoding="UTF-8"):
    """Read and return content from file *path*"""
    with OPEN_FUNC(path, 'rb') as _file:
        cont = _file.read()
        return cont.decode(encoding)

def get(path):
    """Read an object from file"""
    try:
        import cPickle as pickle
    except:
        import pickle

    with open(path, 'rb') as file:
        return pickle.load(file)

def put(path, obj):
    """Write an object to file"""
    try:
        import cPickle as pickle
    except:
        import pickle

    with open(path, 'wb') as file:
        return pickle.dump(obj, file)

def join(*args, **kwargs):
    """Join parts of a path together"""
    import os.path
    if _is_list(args[0]):
        return os.path.join(*args[0])
    return os.path.join(*args, **kwargs)

def cwd():
    """Get or set the current working directory"""
    import os
    return os.getcwd()

def extname(path, **kwargs):
    """Return the extension from *path*"""
    import os.path
    name, ext = os.path.splitext(path, **kwargs)
    return ext

def basename(path, ext=""):
    """Return the file base name from *path*"""
    import os.path
    return os.path.basename(path).replace(ext, "")

def dirname(path):
    """Return the directory name from *path*"""
    import os.path
    return os.path.dirname(path)

""" Aliases """

def append(*args, **kwargs):
    """Alias for fs.write(append=True)"""
    return write(*args, append=True, **kwargs)

def filename(*args, **kwargs):
    """Alias for fs.basename"""
    return basename(*args, **kwargs)

def extension(*args, **kwargs):
    """Alias for fs.extname"""
    return extname(*args, **kwargs)