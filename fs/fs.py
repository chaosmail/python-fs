
"""Helper Functions"""
LIST_TYPE = list
_to_list = lambda e: e if isinstance(e, LIST_TYPE) else [e]

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
    rmfiles(listfiles(path))
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

def abspath(path, **kwargs):
    """Return the absolute path of *path*"""
    import os.path
    return os.path.abspath(path, **kwargs)

def rm(path, **kwargs):
    """Remove *path* which can be either a file
    or a directory"""
    if isfile(path):
        rmfile(path, **kwargs)
    else:
        rmdir(path, **kwargs)

def rmfile(path, **kwargs):
    """Remove the file *path*"""
    import os
    return os.unlink(path, **kwargs)

def rmfiles(paths, **kwargs):
    """Remove an array of files *path*"""
    for p in paths:
        rmfile(p, **kwargs)

def unlink(*args, **kwargs):
    """Unix equivalent *unlink*"""
    return rmfile(*args, **kwargs)

def rmdir(path, recursive=True, **kwargs):
    """Remove the directory *path*"""
    if recursive:
        import shutil
        return shutil.rmtree(path, **kwargs)
    else:
        import os
        return os.remdir(path, **kwargs)

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
    open(path, 'a+').close()

def exists(path, **kwargs):
    """Check if file or directory exists"""
    import os.path
    return os.path.exists(path, **kwargs)

def access(path, **kwargs):
    pass

def list(path='.'):
    """generator that returns all files 
    and directories of *path*"""
    import os
    for f in os.listdir(path):
        yield join(path, f) if path != '.' else f

def listfiles(path='.'):
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
            for filename in fnmatch.filter(listfiles(path), pat):
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

def put(path, content, encoding="UTF-8"):
    """Put *content* to file in *path*"""
    with open(path, 'w+') as _file:
        cont_enc = content.encode(encoding)
        _file.write(content)

def append(path, content, encoding="UTF-8"):
    """Append *content* to file in *path*"""
    with open(path, 'a+') as _file:
        cont_enc = content.encode(encoding)
        _file.write(content)

def get(path, encoding="UTF-8"):
    """Get *content* from file in *path*"""
    with open(path, 'r') as _file:
        cont = _file.read()
        return cont.decode(encoding)

def content(path, content=None, encoding="UTF-8"):
    """Access the content of a file in *path*
    and either *get* or *set* the content"""
    if content:
        put(path, content, encoding)
    else:
        return get(path, encoding)

def join(*args, **kwargs):
    """Join parts of a path together"""
    import os.path
    return os.path.join(*args, **kwargs)

def cwd(path=None, **kwargs):
    """Get or set the current working directory"""
    import os
    if path:
        chdir(path, **kwargs)
    else:
        return os.getcwd(**kwargs)

def extension(path, **kwargs):
    """Return the extension from *path*"""
    import os.path
    name, ext = os.path.splitext(path, **kwargs)
    return ext[1:]

def filename(path, **kwargs):
    """Return the file name from *path*"""
    import os.path
    return os.path.basename(path, **kwargs)

def dirname(path, **kwargs):
    """Return the directory name from *path*"""
    import os.path
    return os.path.dirname(path, **kwargs)