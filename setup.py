#!/usr/bin/env python

from distutils.core import setup

setup(
    name="betterpath",
    version="1.0",
    author="Torstein Sørnes",
    packages=["betterpath"],
    install_requires=[
        "fuzzywuzzy>=0.17.0",
    ],
    zip_safe=False,
)
