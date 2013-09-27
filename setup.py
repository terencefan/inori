# -*- coding: utf-8 -*-
import distutils.sysconfig
import os

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name="sakura",
    version="1.0",
    description="stdrickforce's ubuntu rapid configuration solution",
    long_description=open("README.md").read(),
    author="[STD]Rick_Force",
    author_email="stdrickforce@gmail.com",
    packages=find_packages(),
    pacakage_data={},
    install_requires=[
        "flask>=0.10.1",
        "sqlalchemy>=0.8.0",
    ]
)

site_path = distutils.sysconfig.get_python_lib()
print site_path

f = open("{}/inori.pth".format(site_path), 'w')
f.write(os.getcwd())
f.close()
