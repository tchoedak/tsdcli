import os


def walk_up(path, anchor):
    '''
    Walk up directories until an anchor is found
    '''
    if anchor in os.listdir(path):
        return path
    elif path == '/':
        return None
    else:
        return walk_up(os.path.dirname(path), anchor)


def find_destination(path, anchor):
    '''
    Find the absolute path to a an anchor startin from path
    '''
    parts = anchor.split('/')
    for root, directories, files in os.walk(path):
        for dir_ in directories:
            if dir_ in parts:
                return os.path.abspath(os.path.join(root, dir_))
