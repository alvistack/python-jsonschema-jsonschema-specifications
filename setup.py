# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='jsonschema-specifications',
    version='2023.6.1',
    description='The JSON Schema meta-schemas and vocabularies, exposed as a Registry',
    author='Julian Berman',
    author_email='Julian+jsonschema-specifications@GrayVines.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: File Formats :: JSON :: JSON Schema',
    ],
    install_requires=[
        'importlib-resources>=1.4.0; python_version < "3.9"',
        'referencing>=0.28.0',
    ],
    packages=[
        'jsonschema_specifications',
    ],
    include_package_data=True,
)
