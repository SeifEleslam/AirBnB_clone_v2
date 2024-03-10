#!/usr/bin/python3
"""Archive Web Static"""

from datetime import datetime
from fabric.api import env, put, run, local, runs_once, sudo
env.hosts = ['100.26.160.239', '54.158.197.47']


@runs_once
def do_pack():
    """Pack  the static files into a tgz."""
    try:
        now = datetime.now()
        archive_name = f"web_static_{now.year}{now.month:02d}"
        archive_name += f"{now.day:02d}{now.hour:02d}"
        archive_name += f"{now.minute:02d}{now.second:02d}"
        local("mkdir -p versions")
        local(f"tar -czvf versions/{archive_name}.tgz web_static")
        return f"versions/{archive_name}.tgz"
    except Exception:
        return None


@runs_once
def local_deploy(archive_path: str):
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    try:
        sudo(f'cp ${archive_path} /tmp')
        sudo(f'rm -rf /data/web_static/releases/{name}')
        sudo(f"mkdir -p /data/web_static/releases/{name}")
        sudo(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}")
        sudo(f'rm -rf /tmp/{file}')
        sudo(f"mv -f /data/web_static/releases/{name}/web_static/*\
            /data/web_static/releases/{name}")
        sudo(f'rm -rf /data/web_static/releases/{name}/web_static')
        sudo('rm -rf /data/web_static/current')
        sudo(f'ln -s /data/web_static/releases/{name}/ \
            /data/web_static/current')
        return True
    except Exception:
        return False


def host_deploy(archive_path: str):
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    try:
        put(archive_path, f'/tmp', True)
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


def do_deploy(archive_path: str):
    """Pack  the static files into a tgz."""
    if (len(env.hosts) > 0):
        return host_deploy(archive_path)
    else:
        return local_deploy(archive_path)


def deploy():
    """Deploy the application to production server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
