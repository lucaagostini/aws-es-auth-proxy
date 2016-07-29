import os
from pip.req import parse_requirements
from setuptools import setup

# Setuptools
# https://pythonhosted.org/an_example_pypi_project/setuptools.html

# Classifiers
# https://pypi.python.org/pypi?%3Aaction=list_classifiers

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in install_reqs]


setup(
    name = "aws-es-auth-proxy",
    version = "0.1.5",
    author = "Luca Agostini",
    author_email = "agostini.luca@gmail.com",
    description = ("A simple HTTP proxy to authenticato to AWS Elasticsearch cluster."),
    license = "GPL",
    keywords = "aws elasticsearch auth proxy",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=[
        'aws_es_auth_proxy'
    ],
    include_package_data=True,
    long_description=read('README.txt'),
    classifiers=[
    "Development Status :: 3 - Alpha",
    "Topic :: Internet :: Proxy Servers",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    ],
    install_requires=reqs,
    scripts=['bin/aws-es-auth-proxy'],
 )
