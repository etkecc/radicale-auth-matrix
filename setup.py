#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    desc = fh.read()

setuptools.setup(
    name="radicale_auth_matrix",
    version="0.1.1",
    description="matrix.org authentication plugin for Radicale",
    long_description=desc,
    author="etke.cc",
    url="https://github.com/etkecc/radicale-auth-matrix",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="GPL3+",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins ",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
    ],
)
