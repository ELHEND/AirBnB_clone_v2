#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from fabric.api import *

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Args:
        archive_path: The path to the archive file.
    """

    # Upload the archive file to the `/tmp/` directory of the web server.
    put(archive_path, '/tmp/')

    # Uncompress the archive file to the folder `/data/web_static/releases/<archive filename without extension>` on the web server.
    run('mkdir -p /data/web_static/releases/{}/'.format(os.path.basename(archive_path).split('.')[0]))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(os.path.basename(archive_path), os.path.basename(archive_path).split('.')[0]))

    # Delete the archive file from the web server.
    run('rm /tmp/{}'.format(os.path.basename(archive_path)))

    # Delete the symbolic link `/data/web_static/current` from the web server.
    run('rm -rf /data/web_static/current')

    # Create a new the symbolic link `/data/web_static/current` on the web server, linked to the new version of your code (`/data/web_static/releases/<archive filename without extension>`).
    run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(os.path.basename(archive_path).split('.')[0]))

@task
def deploy():
    """
    Deploys the web application to the web servers.
    """

    # Get the path to the archive file.
    archive_path = 'versions/web_static_20170315003959.tgz'

    # Deploy the web application to the web servers.
    do_deploy(archive_path)

env.hosts = ['52.55.249.213', '54.157.32.137']

