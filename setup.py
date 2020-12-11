#!/usr/bin/env python3
# coding: UTF-8

from setuptools import setup

setup(
    name="aprox",
    version="0.1.0",
    description="Android PROXy setting tool",
    author="Taichi Kotake",
    packages=['aprox'],
    entry_points={
        'console_scripts': [
            'aprox = aprox.cli:main',
        ],
    },
    install_requires=[
        'colorama'
    ],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
