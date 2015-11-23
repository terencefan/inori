#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Tue Sep 15 11:11:24 2015
# Updated At: Tue Sep 15 14:36:54 2015

__author__ = "stdricforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

from fabric.api import (
    cd,
    env,
    hosts,
    local,
    prefix,
    sudo,
    task,
)

from fabric.contrib.files import exists
from fabric.contrib.project import rsync_project

env.sudo_prefix = "sudo su -c"
env.use_ssh_config = True

VENV = 'inorienv'


@task
@hosts(['inori-1'])
def deploy():
    '''
    '''

    # 构建前端文件
    local('gulp deploy')

    # 将文件拷贝到服务器上
    rsync_project(
        local_dir='./', remote_dir='/srv/inori',
        exclude=['node_modules', '.git'], delete=True,
        extra_opts="--rsync-path='sudo rsync'"
    )

    # 安装python-dev
    # sudo('apt-get install python-dev libxml2-dev libxslt-dev --fix-missing')

    # 安装virtualenvo
    sudo('pip install virtualenv')

    # 生成virtualenv
    sudo('mkdir -p /srv/virtualenvs/')
    with cd('/srv/virtualenvs/'):
        if not exists('/srv/virtualenvs/inorienv', use_sudo=True):
            sudo('virtualenv %s --python=/usr/bin/python' % VENV)

    # 安装python packages
    with cd('/srv/inori'):
        with prefix('source /srv/virtualenvs/%s/bin/activate' % VENV):
            sudo('pip install -r requirements.txt')
            sudo('python setup.py install')

    # 其实个人项目应该也可以把nginx和supervisorctl配置写在代码库里

    # 重启服务，大功告成！
    sudo('supervisorctl restart inori')
