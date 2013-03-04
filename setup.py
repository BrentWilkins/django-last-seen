#!/usr/bin/env python

from distutils.core import setup

__author__ = u'Ferran Pegueroles'
__copyright__ = u'Copyright 2013, Ferran Pegueroles'
__credits__ = [u'Ferran Pegueroles']


__license__ = 'GPL'
__version__ = '0.1'
__email__ = 'ferran@pegueroles.com'


long_description = open('README.rst').read()


setup(
    name='django-last-seen',
    version=__version__,
    url='http://bitbucket.org/ferranp/django-last-seen',
    author=__author__,
    author_email=__email__,
    license='GPL',
    packages=['last_seen'],
    description='Keep track of when a user has been last seen',
    long_description=long_description,
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content']
)