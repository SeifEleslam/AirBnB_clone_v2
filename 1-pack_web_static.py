#!/usr/bin/python3
"""Archive Web Static"""
from fabric.operations import local
from datetime import datetime


def do_pack():
    """Pack  the static files into a tgz."""
    now = datetime.now()
    archive_name = f"web_static_{now.year}{now.month:02d}"
    archive_name += f"{now.day:02d}{now.hour:02d}"
    archive_name += f"{now.minute:02d}{now.second:02d}"
    local("mkdir -p versions")
    local(f"tar -czvf versions/{archive_name}.tgz web_static")
