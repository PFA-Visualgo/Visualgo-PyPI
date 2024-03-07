# setup.py

# in case native support for PEP 660 is not available
from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name='visualgo',
    version='2024.3.7',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
