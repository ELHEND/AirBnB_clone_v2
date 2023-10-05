#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
from fabric.api import *

from 2-do_deploy_web_static import do_pack, do_deploy

def deploy():
    """
    Creates and distributes an archive to the web servers.

    Returns:
        True if the deployment was successful, False otherwise.
    """

    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)

env.hosts = ['52.55.249.213', '54.157.32.137']

