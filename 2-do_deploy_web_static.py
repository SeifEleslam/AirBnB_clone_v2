#!/usr/bin/python3
"""Archive Web Static"""

from fabric.api import env, put, run
import os.path

env.hosts = ['100.26.160.239', '54.158.197.47']


# def do_deploy(archive_path: str):
#     """Pack  the static files into a tgz."""

#     try:
#         file = archive_path.split("/")[-1]
#         name = file.split(".")[0]
#         return (
#             put(archive_path, f'/tmp', True).failed is not True and
#             run(f'rm -rf /data/web_static/releases/{name}').failed is not True and
#             run(f"mkdir -p /data/web_static/releases/{name}").failed is not True and
#             run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}").failed is not True and
#             run(f'rm -rf /tmp/{file}').failed is not True and
#             run(f"mv -f /data/web_static/releases/{name}/web_static/* \
#     /data/web_static/releases/{name}").failed is not True and
#             run(f'rm -rf /data/web_static/releases/{name}/web_static').failed is not True and
#             run('rm -rf /data/web_static/current').failed is not True and
#             run(f'ln -s /data/web_static/releases/{name}/ \
#     /data/web_static/current').failed is not True
#         )
#     except Exception:
#         return False

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
