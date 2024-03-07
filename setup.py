# setup.py

# in case native support for PEP 660 is not available
from setuptools import setup, find_packages

setup(
    name='visualgo',
    version='2024.3.6',
    packages=find_packages(include=['visualgo'])
)
