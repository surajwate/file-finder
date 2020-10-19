import os

def scantree(path):
    """Recursively scan a directory tree
    :param str path: path to scan
    :rtype: os.DirEntry
    :return: DirEntry via generator
    """
    for entry in os.scandir(path):
        yield entry
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)


def showfiles(dir):
    for entry in scantree(dir):
        if entry.name.endswith(".md") and entry.is_file():
            print(entry.name, entry.path, entry.is_file())


if __name__ == "__main__":
    pass
