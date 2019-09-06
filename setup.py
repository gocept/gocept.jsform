# This should be only one line. If it must be multi-line, indent the second
# line onwards to keep the PKG-INFO file format intact.
"""Next generation forms in javascript"""

from setuptools import setup, find_packages
import os.path
import json
import sys


def read(path):
    if sys.version_info < (3,):
        f = open(path)
    else:
        f = open(path, encoding='UTF-8')
    text = f.read()
    f.close()
    return text


def project_path(*names):
    return os.path.join(*names)


version = json.loads(read(project_path(
    'src', 'gocept', 'jsform', 'resources', 'bower.json')))['version']


setup(
    name='gocept.jsform',
    version=version,

    install_requires=[
        'cssmin',
        'fanstatic>=1.0a2',
        'js.classy',
        'js.jquery',
        'js.knockout>=3.1.0',
        'setuptools',
    ],

    extras_require={
        'test': [
            'gocept.jasmine>=0.3',
            'gocept.jslint',
            'gocept.testing',
        ],
        'listwidget': [
            'js.bootstrap',
            'js.jqueryui',
        ],
    },

    entry_points={
        'console_scripts': [
            # 'binary-name = gocept.jsform.module:function'
        ],
        'fanstatic.libraries': [
            'gocept.jsform = gocept.jsform.resource:library',
            'gocept.jsform.additional = gocept.jsform.resource:additionals',
        ],
    },

    author=('Sebastian Wehrmann <sw@gocept.com>, '
            'Maik Derstappen <md@derico.de>'),
    author_email='sw@gocept.com',
    license='MIT',
    url='https://github.com/gocept/gocept.jsform',

    keywords='form javascript jquery client',
    classifiers="""\
Development Status :: 7 - Inactive
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 2 :: Only
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.rst',
        'CHANGES.rst',
    )),

    namespace_packages=['gocept'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
)
