#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import re
from setuptools import setup
from setuptools import find_packages


def read_file(filename):
    """Open and a file, read it and return its contents."""
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()


def get_version():
    """Extract and return version number from the packages '__init__.py'."""
    init_path = os.path.join('sppy', '__init__.py')
    content = read_file(init_path)
    match = re.search(r"__version__ = '([^']+)'", content, re.M)
    version = match.group(1)
    return version


setup(
    # Meta-Data
    name='python-systempay-mock',
    version=get_version(),
    author='Bastian Bretagne',
    author_email='bretagne.bastian@gmail.com',
    maintainer='Bastian Bretagne',
    maintainer_email='bretagne.bastian@gmail.com',
    url='https://github.com/bastianb/sppy',
    description=('Python SystemPay Mock is a mock of the systempay'
                 'Payment Form service.'
                 'See: https://systempay.cyberpluspaiement.com/html/'),
    long_description=open('README.md').read(),
    # download_url='#TODO',
    # classifiers='#TODO',
    # platforms='#TODO',
    # license='#TODO',

    # Install config
    packages=find_packages(include=('sppy*',)),
    include_package_data=True,
    install_requires=open('requirements.txt').read(),
    entry_points={
        'console_scripts': [
            'sppy=sppy.scripts.cli:cli'
        ],
    }
)
