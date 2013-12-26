#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

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
    # entry_points
    install_requires=[
        "MySQL-python>=1.2.4",
        "SQLAlchemy>=0.8.3",
        "thrift>=0.9.0",
    ]
)
