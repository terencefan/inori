# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

requires = [
    "celery>=3.0.23",
    "email>=4.0.2",
    "flask>=0.10.1",
    "redis>=2.8.0",
    "requests>=2.0.0",
    "rsa>=3.1.2",
    "sqlalchemy>=0.8.0",
]

setup(
    name="inori",
    version="0.1",
    description="stdrickforce's website",
    long_description=open("README.md").read(),
    author="[STD]Rick_Force",
    author_email="stdrickforce@gmail.com",
    packages=find_packages(),
    url='http://www.stdrickforce.com',
    pacakage_data={},
    install_requires=requires,
)
