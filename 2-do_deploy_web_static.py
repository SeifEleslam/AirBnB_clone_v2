#!/usr/bin/python3
"""Archive Web Static"""

from fabric.operations import put, run
from fabric.api import env

env.hosts = ['100.26.160.239', '54.158.197.47']


def do_deploy(archive_path: str):
    """Pack  the static files into a tgz."""
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    try:
        put(archive_path, f'/tmp', True)
        run(f"mkdir -p /data/web_static/releases/{name}")
        run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}")
        run(f'rm -rf /tmp/{file}')
        run(f"mv /data/web_static/releases/{name}/web_static/*\
            /data/web_static/releases/{name}")
        run(f'rm -rf /data/web_static/releases/{name}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{name}/ \
            /data/web_static/current')
        return True
    except Exception:
        return False
