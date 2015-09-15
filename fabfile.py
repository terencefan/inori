#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Tue Sep 15 11:11:24 2015
# Updated At: Tue Sep 15 13:35:34 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

from fabric.api import (
    cd,
    env,
    hosts,
    local,
    run,
    sudo,
    task,
)

from fabric.contrib.project import rsync_project

env.sudo_prefix = "sudo su -c"
env.use_ssh_config = True

VENV = 'inorienv'


@task
@hosts(['inori-1'])
def deploy():
    '''
    '''

    # 下载前端依赖的libs
    local('bower install')

    # 构建前端文件
    local('gulp deploy')

    # 将文件拷贝到服务器上
    rsync_project(
        local_dir='./', remote_dir='/srv/inori',
        exclude=['node_modules', '.git'], delete=True,
        extra_opts="--rsync-path='sudo rsync'"
    )

    # 安装python-dev
    # sudo('apt-get install python-dev libxml2-dev libxslt-dev')

    # 安装virtualenvo
    sudo('pip install virtualenv')

    # 生成virtualenv
    sudo('mkdir -p /srv/virtualenvs/')
    with cd('/srv/virtualenvs/'):
        sudo('virtualenv %s --python=/usr/bin/python' % VENV)

    # 安装python packages
    run('source /srv/virtualenvs/%s/bin/activate' % VENV)
    with cd('/srv/inori'):
        # sudo('make install')
        sudo('pip install -r requirements.txt')
        sudo('python setup.py install')

    # 其实个人项目应该也可以把nginx和supervisorctl配置写在代码库里

    # 重启服务，大功告成！
    sudo('supervisorctl restart inori')
