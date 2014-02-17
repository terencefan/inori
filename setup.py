#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

entry_points = [
    # general server / helper
    "iserver = inori.core.cmd:server",
    "ihelper = inori.core.cmd:helper",
]

setup(
    name="inori",
    version="1.1.0",
    description="stdrickforce core service.",
    long_description=open("README.md").read(),
    author="stdrickforce",
    author_email="stdrickforce@gmail.com",
    packages=find_packages(),
    # package_data
    url="https://github.com/stdrickforce/inori",
    # license
    entry_points={"console_scripts": entry_points},
    install_requires=[
        "MySQL-python>=1.2.4",
        "SQLAlchemy>=0.8.3",
    ]
)
