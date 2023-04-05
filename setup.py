#!/usr/bin/env python
from setuptools import setup, find_packages

# get regular requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# get dev requirements from dev-requirements.txt
with open('dev-requirements.txt') as f:
    dev_requirements = f.read().splitlines()

setup(
    name="my_project",
    version="0.0.0",
    description='My project description',
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements,
    },
)