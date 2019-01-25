# setup.py
# Added to discover packages and fix issues when alembic runs
# and try to find models from upper and nested folder
from setuptools import setup, find_packages

setup(
    name='matcher',
    packages=find_packages()
)
