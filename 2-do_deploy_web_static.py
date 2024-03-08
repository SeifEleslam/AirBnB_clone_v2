#!/usr/bin/python3
"""Archive Web Static"""

from fabric.api import env, put, run

env.hosts = ['100.26.160.239', '54.158.197.47']


def do_deploy(archive_path: str):
    """Pack  the static files into a tgz."""

    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        return (
            put(archive_path, f'/tmp', True).failed is not True and
            run(f'rm -rf /data/web_static/releases/{name}').failed is not True and
            run(f"mkdir -p /data/web_static/releases/{name}").failed is not True and
            run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}").failed is not True and
            run(f'rm -rf /tmp/{file}').failed is not True and
            run(f"mv -f /data/web_static/releases/{name}/web_static/* \
    /data/web_static/releases/{name}").failed is not True and
            run(f'rm -rf /data/web_static/releases/{name}/web_static').failed is not True and
            run('rm -rf /data/web_static/current').failed is not True and
            run(f'ln -s /data/web_static/releases/{name}/ \
    /data/web_static/current').failed is not True
        )
    except Exception:
        return False
