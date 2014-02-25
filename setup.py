#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import sys, os

__version__ = '0.1'

setup(name='obo',
    version=__version__,
    description="Parser and network representation of Open Biological and Biomedical Ontologies (OBO)",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Environment :: Console",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='obo',
    author='Michael Schubert',
    author_email='mschu.dev@gmail.com',
    url='http://github.com/mschubert/python-obo/',
    license='MIT',
    packages=['obo'],
    package_data={"obo": ["obo/*.py"]}
)

