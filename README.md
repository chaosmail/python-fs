# Python FS - a pythonic file system wrapper for humans

[![Build Status](https://travis-ci.org/chaosmail/python-fs.svg?branch=master)](https://travis-ci.org/chaosmail/python-fs)

An easy to use file system wrapper for Python that aims to simplify os, os.path, os.walk, shutils, fnmatch, etc.

This is under active development!

## Documentation

```python
import fs
```

### fs.exists(path)

Reurns True if the *path* exists. Returns False if *path* does not exist.

```python
>>> fs.exists('test.txt')
True
>>> fs.exists('some_directory')
True
```

### fs.isfile(path)

Reurns True if the *path* exists and is a file. Returns False if *path* is a directory or does not exist.

```python
>>> fs.isfile('test.txt')
True
>>> fs.isfile('some_directory')
False
```

### fs.isdir(path)

Reurns True if the *path* exists and is a directory. Returns False if *path* is a file or does not exist.

```python
>>> fs.isdir('test.txt')
False
>>> fs.isdir('some_directory')
True
```

### fs.rename(oldPath, newPath)

Renames oldPath to new newPath where *oldPath* can be either a file or directory. Raises *OSError* exception if *oldPath* does not exist.

```python
>>> fs.rename('old_test.txt', 'new_test.txt')
>>> fs.rename('old_directory', 'new_directory')
```

### fs.truncate(path)

Removes all files from the *path* directory.

```python
>>> fs.truncate('some_directory')
```

### fs.chdir(path)

Changes the current directory to *path*.

```python
>>> fs.chdir('some_directory')
```

### fs.abspath(path)

Returns the absolute path from a relative *path* where *path* can be either file or directory.

```python
>>> fs.abspath('test.txt')
'/path/to/file/test.txt'
>>> fs.abspath('some_directory')
'/path/to/file/some_directory'
```

### fs.rm(path)

Deletes *path* where *path* can be either a file or directory. Raises an *OSError* exception if *path* does not exist.

```python
>>> fs.rm('test.txt')
>>> fs.rm('some_directory')
```


### fs.unlink(path)

Deletes the file *path*. Raises an *OSError* exception if the file does not exist or *path* is a directory.

```python
>>> fs.unlink('test.txt')
```

### fs.rmdir(path, recursive=True)

Deletes the directory *path* with all containing files and directories. Raises an *OSError* exception if the directory does not exist or *path* is a file.

```python
>>> fs.rmdir('some_directory')
```

### fs.touch(path)

Sets the timestamp of the file *path* to the current time or creates the file if *path* does not exist. Raises an *IOError* exception if *path* is a directory.

```python
>>> fs.touch('test.txt')
```

### fs.list(path='.')

Returns an array of files and directories that are contained in the directory *path*. Raises an *OSError* exception if the directory *path* does not exist.

```python
>>> fs.list()
['some_directory', 'test.txt']
>>> fs.list('some_directory')
['another_test.txt']
```

### fs.listfiles(path='.')

Returns an array of files that are contained in the directory *path*. Raises an *OSError* exception if the directory *path* does not exist.

```python
>>> fs.listfiles()
['test.txt']
>>> fs.listfiles('some_directory')
['another_test.txt']
```

Example: *Loop over all files in the current directory*:

```python
>>> for file in fs.listfiles():
		pass
```

### fs.listdirs(path='.')

Returns an array of directories that are contained in the directory *path*. Raises an *OSError* exception if the directory *path* does not exist.

```python
>>> fs.listdirs()
['some_directory']
>>> fs.listdirs('some_directory')
[]
```

Example: *Loop over all directories in the current directory*:

```python
>>> for dir in fs.listdirs():
		pass
```

### fs.find(pattern, path='.', exclude=None, recursive=True)

Returns an array of files that match *pattern* and are contained in the directory *path*. Both *pattern* and *exclude* can be [Unix shell-style wildcards](https://docs.python.org/3.4/library/fnmatch.html) or arrays of wildcards. Raises an *OSError* exception if the directory *path* does not exist.

```python
>>> fs.find('*.txt')
['/path/to/file/test.txt', '/path/to/file/some_directory/another_test.txt']
>>> fs.find('*.txt', exclude='another*')
['/path/to/file/test.txt']
```

Example: *Loop over all .csv files in the current directory*:

```python
>>> for file in fs.find('*.csv', recursive=False):
		pass
```

Example: *Loop over all .xls and .xlsx files in the current directory and all sub-directories*:

```python
>>> for file in fs.find(['*.xls', '*.xlsx']):
		pass
```

Example: *Loop over all .ini files in the config directory and all sub-directories except the ones starting with local_*:

```python
>>> for file in fs.find('*.ini', path='config', exclude='local_*'):
		pass
```

### fs.finddirs(pattern, path='.', exclude=None, recursive=True)

Returns an array of directories that match *pattern* and are contained in the directory *path*. Both *pattern* and *exclude* can be [Unix shell-style wildcards](https://docs.python.org/3.4/library/fnmatch.html) or arrays of wildcards. Raises an *OSError* exception if the directory *path* does not exist.

```python
>>> fs.finddirs('some*')
['/path/to/file/some_directory']
>>> fs.finddirs('some*', exclude='*directory')
[]
```

### fs.content(path, content=None, encoding="UTF-8")

Returns or sets the content of a file *path*.

```python
>>> fs.content('text.txt')
u'test'
>>> fs.content('text.txt', 'test')
```


### fs.get(path, encoding='UTF-8')

Returns the content of a file *path*. Raises an *IOError* exception if the file *path* does not exist.

```python
>>> fs.get('text.txt')
u'test'
```

### fs.put(path, content, encoding='UTF-8')

Sets the content *content* of a file *path*.

```python
>>> fs.set('text.txt', 'test')
```

### fs.append(path, content, encoding='UTF-8')

Appends the content *content* of a file *path*. Raises an *IOError* exception if the file *path* does not exist.

```python
>>> fs.append('text.txt', 'test')
```

### fs.join(part_of_path, part_of_path, ...)

Joins different parts of a path together.

```python
>>> fs.join('/path/to', 'directory')
```

### fs.cwd(path=None)

Returns or sets the current working directory.

```python
>>> fs.cwd()
'/path/to/directory'
>>> fs.cwd('some_dir')
```

### fs.extension(path)

Returns the extension of a file *path*.

```python
>>> fs.extension('test.txt')
'txt'
```

### fs.filename(path)

Returns the filename of a file *path*.

```python
>>> fs.filename('test.txt')
'test'
```

### fs.dirname(path)

Returns the directory of a file *path*.

```python
>>> fs.dirname('/path/to/file/test.txt')
'/path/to/file'
```

## License

This software is provided under the MIT License.