#!/usr/bin/python3
"""Archive Web Static"""
from fabric.operations import local, put, run
from fabric.api import env

env.hosts = ['100.26.160.239', '54.158.197.47']
env.user = 'ubuntu'


def do_deploy(archive_path: str):
    """Pack  the static files into a tgz."""

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    try:
        put(archive_path, '/tmp/', True)
        run(f"tar -xzf /tmp/{archive_path} -C /data/web_static/releases")
        local(f'rm -rf {archive_path}')
        run(f'ln -sf /data/web_static/releases/{name} /data/web_static/current')
        return True
    except Exception:
        return False
