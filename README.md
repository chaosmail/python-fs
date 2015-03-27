# Python FS - a pythonic file system wrapper for humans

I am trying to create a pythonic file system api, please help me :)

This is under active development!

## Documentation

```python
import fs
```

### isfile(path)

Reurns true if the *path* exists and is a file.

```python
>>> fs.isfile('test.txt')
True
>>> fs.isfile('some_directory')
False
```

## License

This software is provided under the MIT License.