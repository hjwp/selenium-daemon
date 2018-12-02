#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='selenium-daemon',
    version='0.1',
    author='Harry Percival',
    author_email='obeythetestinggoat@gmail.com',
    maintainer='Harry Percival',
    maintainer_email='obeythetestinggoat@gmail.com',
    license='Mozilla Public License 2.0',
    url='https://github.com/hjwp/selenium-daemon',
    description='daemonise selenium for faster tests',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    py_modules=['seleniumdaemon'],
    python_requires='>=3.6',
    install_requires=['selenium'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: Mozilla Public License 2.0',
    ],
    scripts=['./bin/selenium-daemon'],
    entry_points={
    },
)
