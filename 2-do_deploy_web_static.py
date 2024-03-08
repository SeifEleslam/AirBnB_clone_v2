#!/usr/bin/python3
"""Archive Web Static"""

from fabric.api import env, put
import os.path

env.hosts = ['100.26.160.239', '54.158.197.47']

if len(env.hosts) == 0:
    from fabric.api import local as run
else:
    from fabric.api import run


def do_deploy(archive_path: str):
    """Pack  the static files into a tgz."""

    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        put(archive_path, f'/tmp', True)
        run(f'rm -rf /data/web_static/releases/{name}')
        run(f"mkdir -p /data/web_static/releases/{name}")
        run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}")
        run(f'rm -rf /tmp/{file}')
        run(f"mv -f /data/web_static/releases/{name}/web_static/* \
/data/web_static/releases/{name}")
        run(f'rm -rf /data/web_static/releases/{name}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{name}/ \
/data/web_static/current').failed is not True
    except Exception as e:
        print(e)
        return False
