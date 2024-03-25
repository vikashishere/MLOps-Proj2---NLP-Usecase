# This setup file will figure out the constructure file (__init__.py) 
# in every folder and will install that as a local package

from setuptools import find_packages, setup

setup(
    name="hate-speech-classification",
    version="0.0.1",
    author="Vikash Das",
    author_email="vikashdas770@gmail.com",
    packages=find_packages(),
    install_requires=[],
)