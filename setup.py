#!/usr/bin/env python3

from setuptools import setup, find_packages

from nbautoeval.version import version

def contents(localfile):
    import os.path
    full_path = os.path.join(os.path.dirname(__file__), localfile)
    with open(full_path) as f:
        return f.read()

setup(
    name             = "nbautoeval",
    version          = version,
    author           = "Thierry Parmentelat",
    author_email     = "thierry.parmentelat@inria.fr",
    description      = "A mini framework to implementauto-evaluated exercises in notebooks",
    long_description = contents("README.md"),
    license          = "CC BY-SA 4.0",
    keywords         = "jupyter notebooks exercises",
    url              = "https://github.com/parmentelat/nbautoeval",
    packages         = find_packages(),
    classifiers      = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        # pypi won't let then in
        # "Framework :: Jupyter",
    ],
)
