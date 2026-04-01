import os
from os.path import abspath, join, getsize

for top_dir, directories, files in os.walk('.'):
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        print('Full path: {0}, size: {1}'.format(full_path, size))
    break