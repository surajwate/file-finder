# Notes for the package (from python docs)

## [os.scandir(path='.')](https://docs.python.org/3.8/library/os.html?highlight=scandir#os.scandir)

Return an iterator of os.DirEntry objects corresponding to the entries in the directory given by path. The entries are yielded in arbitrary order, and the special entries '.' and '..' are not included. If a file is removed from or added to the directory after creating the iterator, whether an entry for that file be included is unspecified.

This function can also support specifying a file descriptor; the file descriptor must refer to a directory.

The scandir() iterator supports the context manager protocol and has the following method:

### scandir.close()

Close the iterator and free acquired resources.

This is called automatically when the iterator is exhausted or garbage collected, or when an error happens during iterating. However it is advisable to call it explicitly or use the with statement.

~~~python
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)
~~~

## [class os.DirEntry](https://docs.python.org/3.8/library/os.html?highlight=scandir#os.DirEntry)

Object yielded by scandir() to expose the file path and other file attributes of a directory entry.

Attributes and methods on a os.DirEntry instance are as follows:

1. name
2. path
3. inode()
4. is_dir(*, follow_symlinks=True)
5. is_file(*, follow_symlinks=True)
6. is_symlink()
7. stat(*, follow_symlinks=True)
