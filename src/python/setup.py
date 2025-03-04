# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# -------------------------------------------------------------------------
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
from codecs import open
from os import path
import sys

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

_install_requires = [
        'numpy>=1.14.0',
        'pandas>=0.22',
        'scipy>=0.18',
        'scikit-learn>0.19.0',
    ]

# dotnetcore2 package is available only for python 3.x
if sys.version_info.major == 3:
    _install_requires.append('dotnetcore2>=2.1.2')

if sys.version_info[0:2] == (2,7):
    _install_requires.append('decorator')
    _install_requires.append('enum')
    _install_requires.append('funcsigs>=1.0.2')

setup(
    name='nimbusml',

    # Versions should comply with PEP440.  For a discussion on
    # single-sourcing the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.2.1',

    description='NimbusML',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://docs.microsoft.com/en-us/nimbusml',

    # Author details
    author='Microsoft',
    author_email='nimbusml@microsoft.com',

    # Choose your license
    license='All rights reserved',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Specify the Python versions you support here. In particular,
        # ensure that you indicate whether you support Python 2, Python
        # 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='microsoft ml ML.NET machine learning nimbusml',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py,
    # uncomment this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires"
    # vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=_install_requires,
    # Recommended format for setuptools>=36.0 follows, however we use an older
    # version so we have to use a workaroud.
    # 'decorator ; python_version=="2.7"'
    # 'enum ; python_version=="2.7"'
    # 'numpy>=1.14.0',
    # 'pandas>=0.22',
    # 'scipy>=0.18',
    # 'scikit-learn>0.19.0'

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'tests': [
            'nose>=1.3', 'pytest>=4.4.0',
            'graphviz', 'imageio',
        ],
        'dprep': ['azureml-dataprep'],
        'utils': ['graphviz', 'imageio'],
    },

    # If your project's tests need one or more additional packages
    # besides those needed to install it, you can use this option to
    # specify them. It should be a string or list of strings specifying
    # what other distributions need to be present for the package's
    # tests to run. When you run the test command, setuptools will
    # attempt to obtain these (even going so far as to download them
    # using EasyInstall).
    # Note that these required projects will not be installed on the
    # system where the tests are run, but only downloaded to the
    # project's setup directory if they're not already installed locally.
    tests_require=[
        'jupyter_client>=4.4.0',
        'nbconvert>=4.2.0',
        'nose>=1.3',
        'pytest>=4.4.0',
    ],

    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <3.8.*',

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less,
    # then these have to be included in MANIFEST.in as well.
    include_package_data=True,

    package_data={
    },

    # Although 'package_data' is the preferred approach, in some case
    # you may need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing
    # -additional-files # noqa
    # In this case, 'data_file' will be installed into
    # '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and
    #  allow pip to create the appropriate form of executable for the
    # target platform.
    entry_points={
    },
)
