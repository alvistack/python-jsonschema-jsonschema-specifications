# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='jsonschema-specifications',
    version='2024.10.1',
    description='The JSON Schema meta-schemas and vocabularies, exposed as a Registry',
    author_email='Julian Berman <Julian+jsonschema-specifications@GrayVines.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: File Formats :: JSON',
        'Topic :: File Formats :: JSON :: JSON Schema',
    ],
    install_requires=[
        'referencing>=0.31.0',
    ],
    packages=[
        'jsonschema_specifications',
        'jsonschema_specifications.tests',
    ],
    include_package_data=True,
)
