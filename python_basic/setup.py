import os

from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="an_example_pypi_project",
    version="1.0.0",
    author="Test Message",
    author_email="adambacon813@gmail.com",
    description=("An demonstration of how to create, document, and publish "
                 "to the cheese shop a5 pypi.org."),
    keywords="example documentation tutorial",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['python_dto.package_demo'],
    long_description=read('README')
)
