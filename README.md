# Python FS - a pythonic file system wrapper for humans

[![Build Status](https://travis-ci.org/chaosmail/python-fs.svg?branch=master)](https://travis-ci.org/chaosmail/python-fs)
[![Coverage Status](https://coveralls.io/repos/chaosmail/python-fs/badge.svg)](https://coveralls.io/r/chaosmail/python-fs)
[![License](http://img.shields.io/:license-mit-blue.svg)](https://raw.githubusercontent.com/chaosmail/python-fs/master/LICENSE)

An easy to use file system wrapper for Python that aims to simplify os, os.path, os.walk, shutils, fnmatch, etc.

This is under active development!

## Installation

Install with the Python Package Manager *pip* with the following command:

```bash
pip install pyfs
```

Or install from source:

```bash
git clone https://github.com/chaosmail/python-fs.git
cd python-fs
python setup.py install
```

## Documentation

First, import the python-fs module.

```python
import fs
```

### fs.exists(path)

Returns True if the *path* exists. Returns False if *path* does not exist.

```python
>>> fs.exists('test.txt')
True
>>> fs.exists('some_directory')
True
```

### fs.isfile(path)

Returns True if the *path* exists and is a file. Returns False if *path* is a directory or does not exist.

```python
>>> fs.isfile('test.txt')
True
>>> fs.isfile('some_directory')
False
```

### fs.isdir(path)

Returns True if the *path* exists and is a directory. Returns False if *path* is a file or does not exist.

```python
>>> fs.isdir('test.txt')
False
>>> fs.isdir('some_directory')
True
```

### fs.stat(path)

Returns a [stats object](https://docs.python.org/2/library/os.html#os.stat) that contains meta data of *path* where path can be either a file or directory. Raises *OSError* exception if *path* does not exist.

```python
>>> s = fs.stat('test.txt')
>>> s.st_atime
1428162423.839133
>>> s.st_mtime
1427919315.960152
>>> s.st_ctime
1427919315.960152
```

### fs.ctime(path)

Platform dependent; returns time of most recent metadata change on Unix, or the time of creation on Windows of *path* where path can be either a file or directory. Raises *OSError* exception if *path* does not exist.

```python
>>> fs.ctime('test.txt')
1427919315.960152
```

### fs.atime(path)

Returns time of most recent access of *path* where path can be either a file or directory. Raises *OSError* exception if *path* does not exist.

```python
>>> fs.atime('test.txt')
1428162423.839133
```

### fs.mtime(path)

Returns time of most recent content modification of *path* where path can be either a file or directory. Raises *OSError* exception if *path* does not exist.

```python
>>> fs.mtime('test.txt')
1427919315.960152
```

### fs.rename(oldPath, newPath)

Renames *oldPath* to new *newPath* where *oldPath* can be either a file or directory. Raises *OSError* exception if *oldPath* does not exist.

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

### fs.cwd()

Get the current working directory.

```python
>>> fs.cwd()
'/path/to/directory'
```

### fs.abspath(path)

Returns the absolute path from a relative *path* where *path* can be either file or directory.

```python
>>> fs.abspath('test.txt')
'/path/to/file/test.txt'
>>> fs.abspath('some_directory')
'/path/to/file/some_directory'
```

### fs.normalize(path)

Returns the normalized path from a *path* where *path* can be either file or directory.

```python
>>> fs.normalize('test_dir/../test/test.txt')
'test/test.txt'
```

### fs.rm(path)

Deletes the file *path*. Raises an *OSError* exception if the file does not exist or *path* is a directory.

```python
>>> fs.rm('test.txt')
```

The Unix-like *fs.unlink* is the same as *fs.rm*.

### fs.rmdir(path, recursive=True)

Deletes the directory *path* with all containing files and directories. Raises an *OSError* exception if the directory does not exist or *path* is a file.

```python
>>> fs.rmdir('some_directory')
```

### fs.rmfiles(paths)

Deletes an array of files *paths*. Raises an *OSError* exception if a file does not exist or an element of *paths* is a directory.

```python
>>> fs.rmfiles(['test.txt', 'another_file.txt'])
```

Example: *Remove all files from the current directory*:

```python
>>> fs.rmfiles( fs.list() )
```


Example: *Remove all .pyc files from a directory*:

```python
>>> fs.rmfiles( fs.find('*.pyc') )
```

### fs.rmdirs(paths, recursive=True)

Deletes an array of directories *paths* with all containing files and directories. Raises an *OSError* exception if a directory does not exist or an element of *paths* is a file.

```python
>>> fs.rmdirs(['some_directory', 'some_other_dir'])
```

Example: *Remove all directories from the current directory*:

```python
>>> fs.rmdirs( fs.listdirs() )
```


Example: *Remove all directories that start with local_*:

```python
>>> fs.rmdirs( fs.finddirs('local_*') )
```


### fs.touch(path)

Sets the modification timestamp of *path* to the current time or creates the file if *path* does not exist. Directories not supported on Windows.

```python
>>> fs.touch('test.txt')
```

### fs.list(path='.')

Generator that returns all files that are contained in the directory *path*. Raises an *OSError* exception if the directory *path* does not exist.

```python
>>> files = fs.list()
>>> list(files)
['test.txt']
>>> files = fs.list('some_directory')
>>> list(files)
['/path/to/dir/some_directory/another_test.txt']
```

Example: *Loop over all files in the current directory*:

```python
>>> for filename in fs.list():
		pass
```

### fs.listdirs(path='.')

Generator that returns all directories that are contained in the directory *path*. Raises an *OSError* exception if the directory *path* does not exist.

```python
>>> dirs = fs.listdirs()
>>> list(dirs)
['some_directory']
>>> dirs = fs.listdirs('some_directory')
>>> list(dirs)
[]
```

Example: *Loop over all directories in the current directory*:

```python
>>> for dirname in fs.listdirs():
		pass
```

### fs.find(pattern, path='.', exclude=None, recursive=True)

Generator that returns all files that match *pattern* and are contained in the directory *path*. Both *pattern* and *exclude* can be [Unix shell-style wildcards](https://docs.python.org/3.4/library/fnmatch.html) or arrays of wildcards. Raises an *OSError* exception if the directory *path* does not exist.

```python
>>> files = fs.find('*.txt')
>>> list(files)
['/path/to/file/test.txt', '/path/to/file/some_directory/another_test.txt']
>>> files = fs.find('*.txt', exclude='another*')
>>> list(files)
['/path/to/file/test.txt']
```

Example: *Loop over all .csv files in the current directory*:

```python
>>> for filename in fs.find('*.csv', recursive=False):
		pass
```

Example: *Loop over all .xls and .xlsx files in the current directory and all sub-directories*:

```python
>>> for filename in fs.find(['*.xls', '*.xlsx']):
		pass
```

Example: *Loop over all .ini files in the config directory and all sub-directories except the ones starting with local_*:

```python
>>> for filename in fs.find('*.ini', path='config', exclude='local_*'):
		pass
```

Example: *Find and get the Vagrantfile in the config directory*:

```python
>>> filename = next( fs.find('Vagrantfile', path='config'), None)
```

Example: *Find the latest SQL file in the backups directory*:

```python
>>> filename = max( fs.find('*.sql', path='backup'), key=fs.ctime)
```

### fs.finddirs(pattern, path='.', exclude=None, recursive=True)

Generator that returns all directories that match *pattern* and are contained in the directory *path*. Both *pattern* and *exclude* can be [Unix shell-style wildcards](https://docs.python.org/3.4/library/fnmatch.html) or arrays of wildcards. Raises an *OSError* exception if the directory *path* does not exist.

```python
>>> dirs = fs.finddirs('some*')
>>> list(dirs)
['/path/to/file/some_directory']
>>> dirs = fs.finddirs('some*', exclude='*directory')
>>> list(dirs)
[]
```

Example: *Loop over all .git directories in the current directory and all subdirectories*:

```python
>>> for dir in fs.finddirs('.git'):
		pass
```

### fs.open(path, mode='r')

Returns a [file object](https://docs.python.org/2/library/stdtypes.html#bltin-file-objects) of a file *path*. Raises an *IOError* exception if the file *path* does not exist.

```python
>>> file = fs.open('text.txt')
```

Example: *Loop through the lines of a file*

```python
>>> file = fs.open('config.ini', 'r')
>>> for line in file:
		pass
```

### fs.write(path, content, encoding='UTF-8', append=False, raw=False)

Writes the content *content* of a file *path*.

```python
>>> fs.write('text.txt', 'test')
```

Example: *Append content to a file*

```python
>>> fs.write('text.txt', 'test', append=True)
```

Example: *Download an image from an url using [requests](http://docs.python-requests.org/en/latest/) and save it to local disc*:

```python
>>> import requests
>>> res = requests.get(url, stream=True)
>>> fs.write(path, res.raw, raw=True)
```

### fs.read(path, encoding='UTF-8')

Reads and returns the content of a file *path*. Raises an *IOError* exception if the file *path* does not exist.

```python
>>> fs.read('text.txt')
u'test'
```

### fs.put(path, obj)

Writes an object *obj* to a file *path*. Raises an *IOError* exception if the file *path* does not exist.

```python
>>> fs.put('array.dat', [1,2,3,4])
```

Example: *Save a trained SVM classifier using [sklearn](http://scikit-learn.org/) to local disc*:

```python
>>> from sklearn import svm
>>> X = [[0, 0], [1, 1]]
>>> y = [0, 1]
>>> clf = svm.SVC()
>>> clf.fit(X, y)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel='rbf', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
>>> fs.put('svm.dat', clf)
```

### fs.get(path, encoding='UTF-8')

Reads and returns an object from a file *path*. Raises an *IOError* exception if the file *path* does not exist.

```python
>>> fs.get('array.dat')
[1,2,3,4]
```

Example: *Read a trained SVM classifier using [sklearn](http://scikit-learn.org/) from local disc*:

```python
>>> clf = fs.get('svm.dat')
>>> clf.predict([[2., 2.]])
array([1])
```


### fs.sep

The character used by the operating system to separate pathname components. This is '/' for POSIX and '\\\\' for Windows.

```python
>>> fs.sep
'/'
```

### fs.join(paths)

Joins an array of *parts* with *fs.sep*.

```python
>>> fs.join([fs.sep, 'path', 'to', 'directory'])
'/path/to/directory'
```

Additionally, you can also pass the path elements as arguments *fs.join(path, path, ...)*.

```python
>>> fs.join(fs.sep, 'path', 'to', 'directory')
'/path/to/directory'
```

### fs.extname(path)

Returns the extension name of a file *path*.

```python
>>> fs.extname('/path/to/file/test.txt')
'.txt'
```

### fs.basename(path, ext="")

Returns the base name of a file *path*.

```python
>>> fs.basename('/path/to/file/test.txt')
'test.txt'
>>> fs.basename('/path/to/file/test.txt', '.txt')
'test'
```

### fs.dirname(path)

Returns the directory name of a file *path*.

```python
>>> fs.dirname('/path/to/file/test.txt')
'/path/to/file'
```

## Changelog

### 0.0.5

* Added fs.put to store object to disc
* Added fs.get to load object from disc

### 0.0.4

* Fixed errors with fs.find for recurive=False
* Added tests for fs.find and fs.finddirs
* Added coverage badge

### 0.0.3

* Fixed python3 error with fs.read
* Added tests for fs.write and fs.read

### 0.0.2

* Fixed installation error from missing README.md file

### 0.0.1

* Initial upload to PyPi

## License

This software is provided under the MIT License.