#!/usr/bin/python3
"""Archive Web Static"""

from fabric.api import env, run, local
from os.path import join
from os import listdir
env.hosts = ['100.26.160.239', '54.158.197.47']


def do_clean(number=0):
    """Clean the static files."""
    number = int(number)
    local_dir = 'versions'
    remote_dir = '/data/web_static/releases'
    files = run(f"ls -1 {remote_dir}").splitlines()
    files.sort()
    number = 1 if number == 0 or number == 1 else number
    for index in range(len(files) - number):
        file_path = join(remote_dir, files[index])
        print(file_path)
        run(f"rm -rf {file_path}")
    files = [file for file in listdir(
        local_dir)]
    files.sort()
    for index in range(len(files) - number):
        file_path = join(local_dir, files[index])
        print(file_path)
        local(f"rm -rf {file_path}")
