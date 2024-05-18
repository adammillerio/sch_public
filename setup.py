#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="scholar-public",
    version="0.0.1",
    license="MIT",
    description="sch codexes for sch.luphy.net",
    author="Adam Miller",
    author_email="miller@adammiller.io",
    url="https://github.com/adammillerio/sch_public",
    download_url="https://github.com/adammillerio/sch_public/archive/v0.0.1.tar.gz",
    keywords=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["scholar-search"],
)
