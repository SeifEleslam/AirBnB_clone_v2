#!/usr/bin/python3
"""Archive Web Static"""

from fabric.api import env, put, run

env.hosts = ['100.26.160.239', '54.158.197.47', '0.0.0.0']


def do_deploy(archive_path: str):
    """Pack  the static files into a tgz."""

    try:
        put(archive_path, f'/tmp', True)
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        run(f'rm -rf /data/web_static/releases/{name}')
        run(f"mkdir -p /data/web_static/releases/{name}")
        run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}")
        run(f'rm -rf /tmp/{file}')
        run(f"mv -f /data/web_static/releases/{name}/web_static/*\
            /data/web_static/releases/{name}")
        run(f'rm -rf /data/web_static/releases/{name}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{name}/ \
            /data/web_static/current')
        return True
    except Exception:
        return False
