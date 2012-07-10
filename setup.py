#!/bin/env python

import os
from distutils.core import setup

name = 'django_secureform'
version = '0.1'
release = '2'
versrel = version + '-' + release
readme = os.path.join(os.path.dirname(__file__), 'README.rst')
download_url = 'https://github.com/downloads/btimby/django-secureform' \
                           '/' + name + '-' + versrel + '.tar.gz'
long_description = file(readme).read()

setup(
    name = name,
    version = versrel,
    description = 'Provides protection against spammers and scammers.',
    long_description = long_description,
    author = 'Ben Timby',
    author_email = 'btimby@gmail.com',
    maintainer = 'Ben Timby',
    maintainer_email = 'btimby@gmail.com',
    url = 'http://github.com/btimby/django-secureform/',
    download_url = download_url,
    license = 'GPLv3',
    packages = [
        "django_secureform",
        "django_secureform.forms",
    ],
    classifiers = (
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
