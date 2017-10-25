# -*- coding: utf-8 -*-

from setuptools import setup

required = ['numpy']

setup(
    name='lshash',
    packages=['lshash'],
    author='Kay Zhu',
    author_email='me@kayzhu.com',
    maintainer='Kay Zhu',
    maintainer_email='me@kayzhu.com',
    description='A fast Python implementation of locality sensitive hashing with persistance support.',
    requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries',
        ],
)
